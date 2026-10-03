"""Lab 3 Python port of the Algonquin Pet Store product API."""
# AI assistance: Codex helped draft this Flask port and its tests.
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Fixed demo catalog matching the Lab 2 Rust API.
PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.get("/")
def health():
    return jsonify({"service": "product-service", "status": "ok"}), 200

@app.get("/products")
def products():
    return jsonify(PRODUCTS), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "3030")))
