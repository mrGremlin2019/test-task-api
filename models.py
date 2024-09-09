from sqlalchemy import (Boolean, Column, Float, Integer, String, ForeignKey, MetaData)
from sqlalchemy.ext.declarative import declarative_base

# Инициализация метаданных
metadata = MetaData()

# Базовый класс для моделей
Base = declarative_base(metadata=metadata)

# Модель продукта
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)

# Пример другой модели, если потребуется
class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)