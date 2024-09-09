import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

class DatabaseClient:
    def __init__(self):
        # Логгер
        self._logger = logging.getLogger(__name__)

        # Загрузка переменных окружения
        load_dotenv(override=True)

        # Проверка переменной окружения
        db_dpath = os.getenv("DB_DPATH")
        if db_dpath is None:
            raise ValueError("Переменная окружения DB_DPATH не определена в файле .env")

        # Работа с путями через pathlib
        db_path = Path(db_dpath)
        if not db_path.exists():
            db_path.mkdir(parents=True)

        # Путь к файлу БД
        self.db_path = db_path / "data.db"

        # Создание движка SQLAlchemy
        self.engine = create_engine(f"sqlite:///{self.db_path}")

        # Создание сессии
        self._session = sessionmaker(bind=self.engine)

        # Создание таблиц
        Base.metadata.create_all(self.engine)

    def get_session(self):
        try:
            return self._session()
        except Exception as e:
            self._logger.error(f"Ошибка при подключении к базе данных: {e}")
            raise