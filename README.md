# Product Service (CST8915 Lab 3)

This Python and Flask port preserves the Algonquin Pet Store product API used in Lab 2. The original Rust implementation remains in `src/main.rs`; the root-level `app.py` is the Lab 3 version deployed to Azure App Service.

## API

- `GET /` returns a health response for the service.
- `GET /products` returns the same three products, IDs, names, and prices as the Lab 2 Rust service.

## Run and test locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m unittest -v
python app.py
```

The service listens on `0.0.0.0:$PORT`; `PORT` defaults to `3030` for local development. Azure App Service supplies `PORT` and detects the root Flask app in `app.py`. `requirements.txt` declares Flask and Gunicorn.

## First four 12-Factor practices

1. **Codebase:** source is versioned in this separate service repository.
2. **Dependencies:** runtime packages are pinned in `requirements.txt`.
3. **Config:** the port is read from `PORT`; deployment-specific configuration is not hard-coded.
4. **Backing services:** this read-only, fixed demo catalog needs no external database. The companion order service uses RabbitMQ as an attached service configured with `RABBITMQ_CONNECTION_STRING`.

The browser-based Store Front reads `VUE_APP_PRODUCT_SERVICE_URL` when it is built. CORS permits that separate frontend to call this API. No credentials belong in this repository.

## AI-use disclosure

Codex assisted with the Lab 3 Python port, test cases, and documentation. The student should review and understand the implementation before submission.
