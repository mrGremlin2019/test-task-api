from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}

def test_get_products_empty():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_product():
    product_data = {
        "name": "Test Product",
        "price": 100,
        "description": "A test product",
        "category": "Test Category"
    }
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
    assert response.json()["price"] == 100
    assert response.json()["description"] == "A test product"
    assert response.json()["category"] == "Test Category"

def test_get_product():
    # Сначала создаем продукт
    product_data = {
        "name": "Test Product",
        "price": 100,
        "description": "A test product",
        "category": "Test Category"
    }
    create_response = client.post("/products/", json=product_data)
    product_id = create_response.json()["id"]

    # Теперь получаем его
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_get_product_not_found():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}

def test_update_product():
    # Сначала создаем продукт
    product_data = {
        "name": "Test Product",
        "price": 100,
        "description": "A test product",
        "category": "Test Category"
    }
    create_response = client.post("/products/", json=product_data)
    product_id = create_response.json()["id"]

    # Теперь обновляем продукт
    update_data = {
        "name": "Updated Product",
        "price": 150,
        "description": "An updated test product",
        "category": "Updated Category"
    }
    response = client.put(f"/products/{product_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"
    assert response.json()["price"] == 150

def test_update_product_not_found():
    update_data = {
        "name": "Updated Product",
        "price": 150,
        "description": "An updated test product",
        "category": "Updated Category"
    }
    response = client.put("/products/999", json=update_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}

def test_delete_product():
    # Сначала создаем продукт
    product_data = {
        "name": "Test Product",
        "price": 100,
        "description": "A test product",
        "category": "Test Category"
    }
    create_response = client.post("/products/", json=product_data)
    product_id = create_response.json()["id"]

    # Теперь удаляем продукт
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

    # Проверяем, что продукт удален
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}

def test_delete_product_not_found():
    response = client.delete("/products/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}

