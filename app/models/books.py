"""Book model definition."""

from sqlalchemy import Column, String, Integer, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from .base import BaseModel


class Book(BaseModel):
    """Модель книги"""
    __tablename__ = "books"

    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    isbn = Column(String(13), unique=True, index=True)
    average_rating = Column(Float, default=0.0)
    ratings_count = Column(Integer, default=0)

    # Отношения
    author = relationship("Author", backref="books")
    ratings = relationship("Rating", backref="book", cascade="all, delete-orphan")