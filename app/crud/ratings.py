"""CRUD operations for ratings."""

from sqlmodel import Session, select

from app.models.ratings import Rating
from app.schemas.ratings import RatingCreate


def create_rating(db: Session, rating: RatingCreate, user_id: int) -> Rating:
    """Create a new rating in the database."""
    db_rating = Rating(**rating.dict(), user_id=user_id)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating


def get_ratings_by_book(db: Session, book_id: int) -> list[Rating]:
    """Retrieve all ratings for a specific book."""
    statement = select(Rating).where(Rating.book_id == book_id)
    return db.exec(statement).all()
