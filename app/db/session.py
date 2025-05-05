"""Database session configuration."""

from sqlalchemy import create_engine
from sqlmodel import Session

from app.config import settings


DATABASE_URL = settings.database_url
engine = create_engine(DATABASE_URL)
SessionLocal = Session


def get_db():
    """Provide a database session."""
    with SessionLocal(engine) as session:
        yield session