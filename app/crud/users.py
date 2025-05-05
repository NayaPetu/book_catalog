"""CRUD operations for users."""

from datetime import datetime, timedelta
from typing import Union

from jose import jwt
from passlib.context import CryptContext
from sqlmodel import Session, select

from app.config import settings
from app.models.users import User
from app.schemas.users import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_username(db: Session, username: str) -> User | None:
    """Retrieve a user by username."""
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()


def authenticate_user(db: Session, username: str, password: str) -> Union[User, bool]:
    """Authenticate a user by username and password."""
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user


def create_user(db: Session, user: UserCreate) -> User:
    """Create a new user in the database."""
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_access_token(data: dict) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt