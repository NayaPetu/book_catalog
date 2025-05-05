# from sqlalchemy.orm import Session
# from app.models import books as models
# from app.schemas import books as schemas

# def get_books(db: Session, skip: int = 0, limit: int = 10, genre: str = None):
#     query = db.query(models.Book)
#     if genre:
#         query = query.filter(models.Book.genre == genre)
#     return query.offset(skip).limit(limit).all()

# def create_book(db: Session, book: schemas.BookCreate):
#     db_book = models.Book(**book.dict())
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book

# def get_book(db: Session, book_id: int):
#     return db.query(models.Book).filter(models.Book.id == book_id).first()

# def get_books(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Book).offset(skip).limit(limit).all()

# from sqlmodel import Session, select
# from app.models.books import Book
# from app.schemas.books import BookCreate

# def create_book(db: Session, book: BookCreate):
#     db_book = Book(**book.dict())
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book

# def get_book(db: Session, book_id: int):
#     statement = select(Book).where(Book.id == book_id)
#     return db.exec(statement).first()

# def get_books(db: Session, skip: int = 0, limit: int = 100):
#     statement = select(Book).offset(skip).limit(limit)
#     return db.exec(statement).all()


from sqlmodel import Session
from app.models.books import Book
from app.schemas.books import BookCreate
from app.crud.base import create_item, get_item, get_items

def create_book(db: Session, book: BookCreate):
    return create_item(db, Book(**book.dict()))

def get_book(db: Session, book_id: int):
    return get_item(db, Book, book_id)

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return get_items(db, Book, skip, limit)