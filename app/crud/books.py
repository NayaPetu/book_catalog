"""CRUD operations for books."""

from sqlmodel import Session

from app.crud.base import create_item, get_item, get_items
from app.models.books import Book
from app.schemas.books import BookCreate


def create_book(db: Session, book: BookCreate) -> Book:
    """Create a new book in the database."""
    return create_item(db, Book(**book.dict()))


def get_book(db: Session, book_id: int) -> Book | None:
    """Retrieve a book by ID."""
    return get_item(db, Book, book_id)


def get_books(db: Session, skip: int = 0, limit: int = 100) -> list[Book]:
    """Retrieve a list of books with pagination."""
    return get_items(db, Book, skip, limit)
