from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    # Здесь можно настроить проверки для тестирования возвращаемого значения

def test_create_product():
    product_data = {
        "name": "Test Product",
        "price": 100,
        "description": "A test product",
        "category": "Test Category"
    }
    response = client.post("/products/", json=product_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Product"


def test_update_product():
    product_data = {
        "name": "Updated Product",
        "price": 150,
        "category": "Updated Category"
    }
    response = client.put("/products/0", json=product_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"