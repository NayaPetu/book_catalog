# эндпоинты для книг (/books/, /books/{id}/)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.crud import books as crud_books
from app.schemas import books as schemas
from app.db.session import get_db
from app.utils.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[schemas.BookResponse])
def get_books(skip: int = 0, limit: int = 10, genre: str = None, db: Session = Depends(get_db)):
    books = crud_books.get_books(db, skip=skip, limit=limit, genre=genre)
    return books

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_books.create_book(db, book)