# : Эндпоинт для рекомендаций (/recommend/).

# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.db.session import get_db
# from app.schemas import recommend as schemas
# from app.utils.recommend import get_recommendations
# from app.utils.auth import get_current_user

# router = APIRouter()

# @router.get("/", response_model=schemas.RecommendationResponse)
# def read_recommendations(
#     db: Session = Depends(get_db),
#     current_user: str = Depends(get_current_user)
# ):
#     recommendations = get_recommendations(db, current_user)
#     return {"books": recommendations}

from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_db
from app.schemas.recommend import RecommendationResponse
from app.utils.recommend import get_recommendations
from app.utils.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=RecommendationResponse)
def read_recommendations(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    recommendations = get_recommendations(db, current_user)
    return {"books": recommendations}