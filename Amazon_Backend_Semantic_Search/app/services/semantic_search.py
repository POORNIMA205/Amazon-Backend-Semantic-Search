"""Local embedding-based semantic search for Amazon products.

The embedding model is downloaded automatically on the first non-empty search.
Product embeddings are cached in memory and refreshed when product text changes.
"""
from __future__ import annotations

import os
from math import sqrt
from pathlib import Path
from threading import Lock
from typing import Sequence

from fastembed import TextEmbedding

MODEL_NAME = "BAAI/bge-small-en-v1.5"
CACHE_DIR = os.getenv("FASTEMBED_CACHE_PATH", str(Path.home() / ".cache" / "fastembed"))
_model: TextEmbedding | None = None
_model_lock = Lock()
_cache_lock = Lock()
_product_signature: tuple | None = None
_product_vectors: list[list[float]] = []


def _get_model() -> TextEmbedding:
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)
                _model = TextEmbedding(model_name=MODEL_NAME, cache_dir=CACHE_DIR)
    return _model


def _product_text(product) -> str:
    return (f"Product: {product.name}. Category: {product.category or ''}. "
            f"Description: {product.description or ''}.")


def _signature(products: Sequence) -> tuple:
    return tuple((p.id, p.name, p.description or "", p.category or "") for p in products)


def _get_product_vectors(products: list) -> list[list[float]]:
    global _product_signature, _product_vectors
    signature = _signature(products)
    with _cache_lock:
        if signature != _product_signature:
            if not products:
                _product_vectors = []
            else:
                model = _get_model()
                _product_vectors = [[float(value) for value in vector]
                                    for vector in model.passage_embed([_product_text(p) for p in products])]
            _product_signature = signature
        return _product_vectors


def _cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    left_norm = sqrt(sum(value * value for value in left))
    right_norm = sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)


def search_products_semantically(query: str, products: list, limit: int = 10) -> list[dict]:
    """Rank SQLAlchemy Product objects by cosine similarity to a natural-language query."""
    if not products:
        return []
    model = _get_model()
    query_vector = [float(value) for value in next(model.query_embed([query]))]
    product_vectors = _get_product_vectors(products)
    ranked = []
    for product, vector in zip(products, product_vectors):
        ranked.append({
            "id": product.id, "name": product.name, "description": product.description,
            "price": product.price, "category": product.category, "stock": product.stock,
            "image_url": product.image_url,
            "similarity_score": round(_cosine_similarity(query_vector, vector), 4),
        })
    ranked.sort(key=lambda item: item["similarity_score"], reverse=True)
    return ranked[:limit]
