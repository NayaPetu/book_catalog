"""Recommendation model definition."""

from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import BaseModel


class Recommendation(BaseModel):
    """Модель рекомендаций книг"""
    __tablename__ = "recommendations"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    score = Column(Float, nullable=False)

    # Отношения
    user = relationship("User", backref="recommendations")
    book = relationship("Book", backref="recommendations")