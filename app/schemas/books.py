"""Pydantic schemas for books."""

from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    """Base schema for books."""

    title: str
    author_id: int
    genre: Optional[str] = None
    publication_year: Optional[int] = None

    def get_title(self) -> str:
        """Return the book's title."""
        return self.title


class BookCreate(BookBase):
    """Schema for creating a book."""

    def validate_title(self) -> bool:
        """Validate the book's title."""
        return len(self.title) > 0


class BookResponse(BookBase):
    """Schema for book response."""

    id: int

    def get_id(self) -> int:
        """Return the book's ID."""
        return self.id

    class Config:
        """Pydantic configuration."""
        from_attributes = True