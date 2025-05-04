# Алгоритм рекомендаций

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Book, Rating
from sqlalchemy import func

router = APIRouter()

class RecommendRequest(BaseModel):
    genre: str | None = None
    author_id: int | None = None
    min_rating: float = 3.0
    limit: int = 10

class BookRecommendation(BaseModel):
    book_id: int
    title: str
    author: str
    genre: str
    avg_rating: float
    score: float

@router.post("/recommend/", response_model=list[BookRecommendation])
def recommend_books(request: RecommendRequest, db: Session = Depends(get_db)):
    # Calculate global average rating (C) and minimum votes (m)
    C = db.query(func.avg(Rating.rating)).scalar() or 3.5
    m = 5

    # Build query
    query = (
        db.query(
            Book.book_id,
            Book.title,
            Book.genre,
            Book.author_id,
            func.avg(Rating.rating).label("avg_rating"),
            func.count(Rating.rating).label("vote_count")
        )
        .outerjoin(Rating, Book.book_id == Rating.book_id)
        .group_by(Book.book_id, Book.title, Book.genre, Book.author_id)
    )

    # Apply filters
    if request.genre:
        query = query.filter(Book.genre == request.genre)
    if request.author_id:
        query = query.filter(Book.author_id == request.author_id)
    query = query.having(func.avg(Rating.rating) >= request.min_rating)

    # Fetch results
    results = query.all()

    # Calculate Bayesian average and sort
    recommendations = []
    for book in results:
        v = book.vote_count
        avg_rating = book.avg_rating or 0
        score = (v * avg_rating + m * C) / (v + m) if v > 0 else 0
        recommendations.append(
            BookRecommendation(
                book_id=book.book_id,
                title=book.title,
                author=db.query(Author).get(book.author_id).name,
                genre=book.genre,
                avg_rating=avg_rating,
                score=score
            )
        )

    # Sort by score and limit
    recommendations.sort(key=lambda x: x.score, reverse=True)
    return recommendations[:request.limit]