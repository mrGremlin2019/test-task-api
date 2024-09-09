from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db_client import DatabaseClient
from models import Product

app = FastAPI()

# Инициализируем клиента базы данных
db_client = DatabaseClient()

# Получение сессии
def get_db():
    db = db_client.get_session()
    try:
        yield db
    finally:
        db.close()

# Создание продукта
@app.post("/products/")
def create_product(name: str, price: float, description: str, category: str, db: Session = Depends(get_db)):
    product = Product(name=name, price=price, description=description, category=category)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Получение всех продуктов
@app.get("/products/")
def read_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# Получение продукта по ID
@app.get("/products/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


# Обновление продукта по ID
@app.put("/products/{product_id}")
def update_product(product_id: int, name: str, price: float, description: str, category: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = name
    product.price = price
    product.description = description
    product.category = category
    db.commit()
    db.refresh(product)
    return product

# Удаление продукта по ID
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return product
