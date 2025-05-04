# Эндпоинты для регистрации, логина, получения профиля (/users/register/, /users/login/, /users/me/).

# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from app.db.session import get_db
# from app.schemas import users as schemas
# from app.crud import users as crud_users
# from app.utils.auth import oauth2_scheme
# from jose import jwt
# from app.config import settings

# router = APIRouter()

# @router.post("/login")
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = crud_users.authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = crud_users.create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud_users.get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     return crud_users.create_user(db, user)

# @router.get("/me", response_model=schemas.UserResponse)
# def read_users_me(current_user: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     user = crud_users.get_user_by_username(db, username=current_user)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from app.db.session import get_db
from app.schemas.users import UserCreate, UserResponse
from app.crud.users import get_user_by_username, authenticate_user, create_user, create_access_token
from app.utils.auth import oauth2_scheme

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=current_user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user