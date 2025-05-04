# Создание, чтение, обновление, удаление пользователей.

# from sqlalchemy.orm import Session
# from app.models import users as models
# from app.schemas import users as schemas
# from passlib.context import CryptContext
# from jose import jwt
# from app.config import settings
# from datetime import datetime, timedelta

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def get_user_by_username(db: Session, username: str):
#     return db.query(models.User).filter(models.User.username == username).first()

# def authenticate_user(db: Session, username: str, password: str):
#     user = get_user_by_username(db, username)
#     if not user:
#         return False
#     if not pwd_context.verify(password, user.hashed_password):
#         return False
#     return user

# def create_user(db: Session, user: schemas.UserCreate):
#     hashed_password = pwd_context.hash(user.password)
#     db_user = models.User(username=user.username, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=30)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
#     return encoded_jwt



from sqlmodel import Session, select
from app.models.users import User
from app.schemas.users import UserCreate
from passlib.context import CryptContext
from jose import jwt
from app.config import settings
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    statement = select(User).where(User.username == username)
    return db.exec(statement).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt