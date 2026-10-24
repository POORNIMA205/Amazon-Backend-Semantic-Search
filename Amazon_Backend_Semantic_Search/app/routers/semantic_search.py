"""Semantic product search endpoint."""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import Product
from app.services.semantic_search import search_products_semantically

router = APIRouter(prefix="/api/search", tags=["Semantic Search"])


@router.get("/products")
def semantic_product_search(
    q: str = Query(..., min_length=2, max_length=300, description="Natural-language product search query"),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    """Find products by meaning, not only exact product-name keywords."""
    products = db.query(Product).all()
    results = search_products_semantically(q.strip(), products, limit)
    return {"query": q, "count": len(results), "results": results}
