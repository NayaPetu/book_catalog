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

# from fastapi import APIRouter, Depends
# from sqlmodel import Session
# from app.db.session import get_db
# from app.schemas.recommend import RecommendationResponse
# from app.utils.recommend import get_recommendations
# from app.utils.auth import get_current_user

# router = APIRouter()

# @router.get("/", response_model=RecommendationResponse)
# def read_recommendations(
#     db: Session = Depends(get_db),
#     current_user: str = Depends(get_current_user)
# ):
#     recommendations = get_recommendations(db, current_user)
#     return {"books": recommendations}


from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_db
from app.schemas.recommend import RecommendationResponse, RecommendCreate
from app.crud.recommend import create_recommend, get_recommend
from app.utils.recommend import get_recommendations
from app.utils.auth import get_current_user
from app.models.users import User
from sqlmodel import select

router = APIRouter()

@router.post("/", response_model=RecommendationResponse, status_code=201)
def create_recommendation(
    recommend: RecommendCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.exec(select(User).where(User.username == current_user)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db_recommend = create_recommend(db, recommend, user.id)
    recommendations = get_recommendations(db, current_user)
    return {"books": recommendations}

@router.get("/", response_model=RecommendationResponse)
def read_recommendations(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    recommendations = get_recommendations(db, current_user)
    return {"books": recommendations}