"""Router for rating-related endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.crud.ratings import create_rating, get_ratings_by_book
from app.db.session import get_db
from app.models.ratings import Rating
from app.models.users import User
from app.schemas.ratings import RatingCreate, RatingResponse
from app.utils.auth import get_current_user


router = APIRouter()


@router.post("/", response_model=RatingResponse, status_code=201)
def create_rating_endpoint(
    rating: RatingCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """Create a new rating."""
    user = db.exec(select(User).where(User.username == current_user)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return create_rating(db, rating, user.id)


@router.get("/book/{book_id}", response_model=List[RatingResponse])
def read_ratings(book_id: int, db: Session = Depends(get_db)):
    """Retrieve all ratings for a specific book."""
    return get_ratings_by_book(db, book_id)


@router.put("/{rating_id}", response_model=RatingResponse)
def update_rating(
    rating_id: int,
    rating: RatingCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """Update a rating by ID."""
    user = db.exec(select(User).where(User.username == current_user)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db_rating = db.exec(select(Rating).where(Rating.id == rating_id, Rating.user_id == user.id)).first()
    if not db_rating:
        raise HTTPException(status_code=404, detail="Rating not found or not owned by user")
    for key, value in rating.dict().items():
        setattr(db_rating, key, value)
    db.commit()
    db.refresh(db_rating)
    return db_rating


@router.delete("/{rating_id}", status_code=204)
def delete_rating(
    rating_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """Delete a rating by ID."""
    user = db.exec(select(User).where(User.username == current_user)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db_rating = db.exec(select(Rating).where(Rating.id == rating_id, Rating.user_id == user.id)).first()
    if not db_rating:
        raise HTTPException(status_code=404, detail="Rating not found or not owned by user")
    db.delete(db_rating)
    db.commit()
