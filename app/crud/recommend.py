"""CRUD operations for recommendations."""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.recommend import Recommendation
from app.schemas.recommend import RecommendCreate, RecommendUpdate

def create_recommend(db: Session, recommend: RecommendCreate) -> Recommendation:
    """Create a new recommendation."""
    db_recommend = Recommendation(
        user_id=recommend.user_id,
        book_id=recommend.book_id,
        score=recommend.score
    )
    db.add(db_recommend)
    db.commit()
    db.refresh(db_recommend)
    return db_recommend

def get_recommend(db: Session, recommend_id: int) -> Optional[Recommendation]:
    """Get a recommendation by ID."""
    return db.query(Recommendation).filter(Recommendation.id == recommend_id).first()

def get_recommends(db: Session, skip: int = 0, limit: int = 100) -> List[Recommendation]:
    """Get all recommendations with pagination."""
    return db.query(Recommendation).offset(skip).limit(limit).all()

def get_user_recommends(db: Session, user_id: int) -> List[Recommendation]:
    """Get all recommendations for a specific user."""
    return db.query(Recommendation).filter(Recommendation.user_id == user_id).all()

def update_recommend(
    db: Session, 
    recommend_id: int, 
    recommend: RecommendUpdate
) -> Optional[Recommendation]:
    """Update a recommendation."""
    db_recommend = get_recommend(db, recommend_id)
    if db_recommend:
        for key, value in recommend.dict(exclude_unset=True).items():
            setattr(db_recommend, key, value)
        db.commit()
        db.refresh(db_recommend)
    return db_recommend

def delete_recommend(db: Session, recommend_id: int) -> bool:
    """Delete a recommendation."""
    db_recommend = get_recommend(db, recommend_id)
    if db_recommend:
        db.delete(db_recommend)
        db.commit()
        return True
    return False