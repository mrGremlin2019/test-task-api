from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    category: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Временное хранилище для продуктов
products = []

# Создание продукта
@app.post("/products/", status_code=201)
def create_product(product: Product):
    products.append(product)
    return product

# Получение всех продуктов
@app.get("/products/", response_model=List[Product])
def get_products():
    return products

# Получение продукта по ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    try:
        return products[product_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Product not found")

# Обновление продукта по ID
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    try:
        products[product_id] = product
        return product
    except IndexError:
        raise HTTPException(status_code=404, detail="Product not found")

# Удаление продукта по ID
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    try:
        product = products.pop(product_id)
        return product
    except IndexError:
        raise HTTPException(status_code=404, detail="Product not found")