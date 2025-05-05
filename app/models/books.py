"""Book model definition."""

from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Book(SQLModel, table=True):
    """Book database model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    genre: Optional[str] = None
    publication_year: Optional[str] = None
    author_id: int = Field(foreign_key="author.id")

    author: Optional["Author"] = Relationship(back_populates="books")