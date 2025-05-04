# эндпоинты для рейтингов (/ratings/, /ratings/{id}/).

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app.db.session import get_db
# from app.schemas import ratings as schemas
# from app.crud import ratings as crud_ratings
# from app.utils.auth import get_current_user

# router = APIRouter()

# @router.post("/", response_model=schemas.RatingResponse, status_code=201)
# def create_rating(
#     rating: schemas.RatingCreate,
#     db: Session = Depends(get_db),
#     current_user: str = Depends(get_current_user)
# ):
#     user = db.query(models.User).filter(models.User.username == current_user).first()
#     return crud_ratings.create_rating(db, rating, user.id)

# @router.get("/book/{book_id}", response_model=List[schemas.RatingResponse])
# def read_ratings(book_id: int, db: Session = Depends(get_db)):
#     ratings = crud_ratings.get_ratings_by_book(db, book_id)
#     return ratings


from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.db.session import get_db
from app.schemas.ratings import RatingCreate, RatingResponse
from app.crud.ratings import create_rating, get_ratings_by_book
from app.utils.auth import get_current_user
from app.models.users import User

router = APIRouter()

@router.post("/", response_model=RatingResponse, status_code=201)
def create_rating_endpoint(
    rating: RatingCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.exec(select(User).where(User.username == current_user)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return create_rating(db, rating, user.id)

@router.get("/book/{book_id}", response_model=List[RatingResponse])
def read_ratings(book_id: int, db: Session = Depends(get_db)):
    ratings = get_ratings_by_book(db, book_id)
    return ratings