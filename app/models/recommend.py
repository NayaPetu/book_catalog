"""Recommendation model definition."""

from typing import Optional

from sqlmodel import Field, SQLModel


class Recommend(SQLModel, table=True):
    """Recommendation database model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    book_id: int = Field(foreign_key="book.id")