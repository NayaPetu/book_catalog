"""Author model definition."""

from typing import List, Optional

from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from .base import BaseModel


class Author(BaseModel):
    """Модель автора"""
    __tablename__ = "authors"

    name = Column(String(255), nullable=False, index=True)
    biography = Column(Text, nullable=True)
    country = Column(String(100), nullable=True)
    
    # Отношения
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")