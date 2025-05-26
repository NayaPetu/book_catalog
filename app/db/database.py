"""Database connection and session management."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings
from app.models.base import Base

# Создаем движок базы данных
engine = create_engine(settings.database_url)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """
    Получение сессии базы данных.
    Используется как зависимость в FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """Создание всех таблиц в базе данных."""
    Base.metadata.create_all(bind=engine) 