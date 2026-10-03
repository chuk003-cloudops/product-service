"""Contract checks for the Python Lab 3 product-service port."""
import unittest
from app import app

class ProductServiceTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"service": "product-service", "status": "ok"})

    def test_products_preserve_lab2_contract(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [
            {"id": 1, "name": "Dog Food", "price": 19.99},
            {"id": 2, "name": "Cat Food", "price": 34.99},
            {"id": 3, "name": "Bird Seeds", "price": 10.99},
        ])

    def test_products_allow_storefront_cors(self):
        response = self.client.get("/products")
        self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
        self.assertIn("GET", response.headers["Access-Control-Allow-Methods"])

    def test_unknown_path_is_not_found(self):
        self.assertEqual(self.client.get("/missing").status_code, 404)

if __name__ == "__main__":
    unittest.main()
