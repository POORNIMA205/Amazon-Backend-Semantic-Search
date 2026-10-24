# Amazon Backend + Semantic Search + Reverse Proxy

This is the complete Amazon backend project with semantic product search integrated into the existing FastAPI app. Open this folder directly in VS Code. You do not need the separate patch folder or installer.

## Semantic Search endpoint

`GET /api/search/products?q=gift%20for%20someone%20who%20loves%20music&limit=10`

The endpoint embeds the query and each product's name, category, and description using `BAAI/bge-small-en-v1.5`, then ranks products by cosine similarity. Existing endpoints, including `/api/products/`, remain in place. The first semantic search downloads the embedding model, so the first run requires internet access. The model cache is stored in the Docker named volume at `/data/fastembed_cache`.

## Run with VS Code and Docker Desktop

1. Extract the ZIP to a folder such as `Downloads/Amazon_Backend_Semantic_Search`.
2. Open that extracted folder in VS Code using **File → Open Folder**.
3. Start Docker Desktop and wait until it is running.
4. Open **Terminal → New Terminal** in VS Code. Ensure the terminal is at this project's root (the same folder as `docker-compose.yml`).
5. Validate configuration:

   ```powershell
   docker compose config
   ```

6. Build and start the app:

   ```powershell
   docker compose up --build -d
   ```

7. Check services and logs:

   ```powershell
   docker compose ps
   docker compose logs --tail=100 app
   ```

8. Open Swagger: http://localhost/docs

9. Test semantic search in PowerShell:

   ```powershell
   Invoke-RestMethod -Method Get -Uri "http://localhost/api/search/products?q=headphones%20for%20travelling&limit=10"
   ```

If port 80 is already occupied by another project/container, stop and resolve that conflict before starting this project's `nginx` service. Do not delete Docker volumes: the `app_data` volume contains the database and model cache for this Compose project.

## Run locally without Docker (optional)

Use Python 3.11, create/activate a virtual environment, install requirements, then run `uvicorn app.main:app --reload`. Make sure `.env` is configured for your local database.

## Important notes

- This ZIP was assembled from the backend source you attached. The bundled `.conda` environment and generated logs were excluded to keep the project portable; Docker builds its own environment from `requirements.txt`.
- The included `amazon.db` is the database from the uploaded ZIP. On the first Docker start only, the container copies it into the named `app_data` volume if that volume does not already contain a database; later starts preserve the volume database.
- `.env` is a starter configuration. Replace the placeholder `SECRET_KEY` before deployment and never publish secrets to GitHub.
- The existing reverse-proxy configuration was placed under `nginx/`, which is the path referenced by `docker-compose.yml`.
