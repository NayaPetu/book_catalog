"""User model definition."""

from typing import Optional

from sqlalchemy import Column, String, Boolean
from .base import BaseModel


class User(BaseModel):
    """Модель пользователя"""
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)