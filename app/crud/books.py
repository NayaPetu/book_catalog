from sqlalchemy.orm import Session
from app.models import books as models
from app.schemas import books as schemas

def get_books(db: Session, skip: int = 0, limit: int = 10, genre: str = None):
    query = db.query(models.Book)
    if genre:
        query = query.filter(models.Book.genre == genre)
    return query.offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book