# from sqlalchemy.orm import Session
# from app.models import ratings as models
# from app.schemas import ratings as schemas

# def create_rating(db: Session, rating: schemas.RatingCreate, user_id: int):
#     db_rating = models.Rating(**rating.dict(), user_id=user_id)
#     db.add(db_rating)
#     db.commit()
#     db.refresh(db_rating)
#     return db_rating

# def get_ratings_by_book(db: Session, book_id: int):
#     return db.query(models.Rating).filter(models.Rating.book_id == book_id).all()

from sqlmodel import Session, select
from app.models.ratings import Rating
from app.schemas.ratings import RatingCreate

def create_rating(db: Session, rating: RatingCreate, user_id: int):
    db_rating = Rating(**rating.dict(), user_id=user_id)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_ratings_by_book(db: Session, book_id: int):
    statement = select(Rating).where(Rating.book_id == book_id)
    return db.exec(statement).all()