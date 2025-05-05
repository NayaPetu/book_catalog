"""Rating model definition."""

from typing import Optional

from sqlmodel import Field, SQLModel


class Rating(SQLModel, table=True):
    """Rating database model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    score: int
    user_id: int = Field(foreign_key="user.id")
    book_id: int = Field(foreign_key="book.id")