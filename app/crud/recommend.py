"""CRUD operations for recommendations."""

from sqlmodel import Session, select

from app.models.recommend import Recommend
from app.schemas.recommend import RecommendCreate


def create_recommend(db: Session, recommend: RecommendCreate, user_id: int) -> Recommend:
    """Create a new recommendation in the database."""
    db_recommend = Recommend(**recommend.dict(), user_id=user_id)
    db.add(db_recommend)
    db.commit()
    db.refresh(db_recommend)
    return db_recommend


def get_recommend(db: Session, book_id: int) -> list[Recommend]:
    """Retrieve recommendations for a specific book."""
    statement = select(Recommend).where(Recommend.book_id == book_id)
    return db.exec(statement).all()