"""Rating model definition."""

from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from .base import BaseModel


class Rating(BaseModel):
    """Модель рейтинга книги"""
    __tablename__ = "ratings"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    rating = Column(Float, nullable=False)
    review = Column(Text, nullable=True)

    # Отношения
    user = relationship("User", backref="ratings")
    book = relationship("Book", back_populates="ratings")