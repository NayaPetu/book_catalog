# эндпоинты для книг (/books/, /books/{id}/)

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List
# from app.crud import books as crud_books
# from app.schemas import books as schemas
# from app.db.session import get_db
# from app.utils.auth import get_current_user

# router = APIRouter()

# @router.get("/", response_model=List[schemas.BookResponse])
# def get_books(skip: int = 0, limit: int = 10, genre: str = None, db: Session = Depends(get_db)):
#     books = crud_books.get_books(db, skip=skip, limit=limit, genre=genre)
#     return books

# @router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
# def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
#     return crud_books.create_book(db, book)


# from fastapi import APIRouter, Depends, HTTPException
# from sqlmodel import Session
# from typing import List
# from app.db.session import get_db
# from app.schemas.books import BookCreate, BookResponse
# from app.crud.books import create_book, get_book, get_books

# router = APIRouter()

# @router.post("/", response_model=BookResponse, status_code=201)
# def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
#     return create_book(db, book)

# @router.get("/", response_model=List[BookResponse])
# def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return get_books(db, skip, limit)

# @router.get("/{book_id}", response_model=BookResponse)
# def read_book(book_id: int, db: Session = Depends(get_db)):
#     book = get_book(db, book_id)
#     if book is None:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return book


from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.db.session import get_db
from app.schemas.books import BookCreate, BookResponse
from app.crud.books import create_book, get_book, get_books

router = APIRouter()

@router.post("/", response_model=BookResponse, status_code=201)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/", response_model=List[BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_books(db, skip, limit)

@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
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
    db_book = get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return None