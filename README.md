# FastAPI Product Management API

## Описание
Это API для управления продуктами на торговой площадке.

## Установка
1. Убедитесь, что установлен [Poetry](https://python-poetry.org/).
2. Установите зависимости:
   ```bash
   poetry install

## API
1. Создание продукта
   ```bash
   POST /products/

Тело запроса::
   ```json{
     {
      "name": "Test Product",
      "price": 100.0,
      "description": "A test product",
      "category": "Test Category"
     }
   ```
2. Получение всех продуктов
   ```bash
   GET /products/
3. Получение продукта по ID:
   ```bash
   GET /products/{product_id}

4. Обновление продукта
   ```bash
   PUT /products/{product_id}

Тело запроса:
   ```json{
    {
      "name": "Updated Product",
      "price": 150.0,
      "description": "Updated description",
      "category": "Updated Category"
    }
```
5. Удаление продукта
    ```bash
    DELETE /products/{product_id}
   

Этот файл включает описание проекта, инструкции по установке и запуску, а также примеры запросов к API.