
"""CRUD operations for authors."""

from sqlmodel import Session

from app.crud.base import create_item, get_item, get_items
from app.models.authors import Author
from app.schemas.authors import AuthorCreate


def create_author(db: Session, author: AuthorCreate) -> Author:
    """Create a new author in the database."""
    return create_item(db, Author(**author.dict()))


def get_author(db: Session, author_id: int) -> Author | None:
    """Retrieve an author by ID."""
    return get_item(db, Author, author_id)


def get_authors(db: Session, skip: int = 0, limit: int = 100) -> list[Author]:
    """Retrieve a list of authors with pagination."""
    return get_items(db, Author, skip, limit)