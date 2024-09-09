# Используем базовый образ Python 3.10
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей проекта
COPY pyproject.toml poetry.lock /app/

# Устанавливаем Poetry для управления зависимостями
RUN pip install poetry

# Устанавливаем зависимости проекта
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Копируем всё содержимое текущей директории в контейнер
COPY . /app

# Открываем порт 8000 для FastAPI
EXPOSE 8000

# Команда для запуска сервиса FastAPI через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
