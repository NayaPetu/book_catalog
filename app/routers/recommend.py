"""Router for recommendations."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.recommend import (
    create_recommend,
    get_recommend,
    get_recommends,
    get_user_recommends,
    update_recommend,
    delete_recommend
)
from app.schemas.recommend import Recommend, RecommendCreate, RecommendUpdate
from app.db.database import get_db
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=Recommend)
def create_recommendation(
    recommend: RecommendCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Create a new recommendation."""
    return create_recommend(db=db, recommend=recommend)

@router.get("/{recommend_id}", response_model=Recommend)
def read_recommendation(recommend_id: int, db: Session = Depends(get_db)):
    """Get a recommendation by ID."""
    db_recommend = get_recommend(db, recommend_id)
    if db_recommend is None:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return db_recommend

@router.get("/", response_model=List[Recommend])
def read_recommendations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all recommendations."""
    return get_recommends(db, skip=skip, limit=limit)

@router.get("/user/{user_id}", response_model=List[Recommend])
def read_user_recommendations(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get recommendations for a specific user."""
    return get_user_recommends(db, user_id)

@router.put("/{recommend_id}", response_model=Recommend)
def update_recommendation(
    recommend_id: int,
    recommend: RecommendUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Update a recommendation."""
    db_recommend = update_recommend(db, recommend_id, recommend)
    if db_recommend is None:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return db_recommend

@router.delete("/{recommend_id}")
def delete_recommendation(
    recommend_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Delete a recommendation."""
    if not delete_recommend(db, recommend_id):
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return {"ok": True}

# # : Эндпоинт для рекомендаций (/recommend/).

# from fastapi import APIRouter, Depends, HTTPException
# from sqlmodel import Session
# from app.db.session import get_db
# from app.schemas.recommend import RecommendationResponse, RecommendCreate
# from app.crud.recommend import create_recommend, get_recommend
# from app.utils.recommend import get_recommendations
# from app.utils.auth import get_current_user
# from app.models.users import User
# from sqlmodel import select

# router = APIRouter()

# @router.post("/", response_model=RecommendationResponse, status_code=201)
# def create_recommendation(
#     recommend: RecommendCreate,
#     db: Session = Depends(get_db),
#     current_user: str = Depends(get_current_user)
# ):
#     user = db.exec(select(User).where(User.username == current_user)).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     db_recommend = create_recommend(db, recommend, user.id)
#     recommendations = get_recommendations(db, current_user)
#     return {"books": recommendations}

# @router.get("/", response_model=RecommendationResponse)
# def read_recommendations(
#     db: Session = Depends(get_db),
#     current_user: str = Depends(get_current_user)
# ):
#     recommendations = get_recommendations(db, current_user)
#     return {"books": recommendations}