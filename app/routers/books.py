"""Router for book-related endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud.books import create_book, get_book, get_books
from app.db.session import get_db
from app.schemas.books import BookCreate, BookResponse


router = APIRouter()


@router.post("/", response_model=BookResponse, status_code=201)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    """Create a new book."""
    return create_book(db, book)


@router.get("/", response_model=List[BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a list of books."""
    return get_books(db, skip, limit)


@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """Retrieve a book by ID."""
    book = get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    """Update a book by ID."""
    db_book = get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID."""
    db_book = get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()