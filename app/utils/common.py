from typing import Optional, TypeVar, Callable, Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

T = TypeVar('T')

def get_object_or_404(
    db: Session,
    model: Callable,
    id: int,
    error_message: str = "Объект не найден"
) -> T:
    """
    Получает объект из базы данных или возвращает 404 ошибку
    """
    db_obj = db.query(model).filter(model.id == id).first()
    if db_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_message
        )
    return db_obj

def check_object_exists(
    db: Session,
    model: Callable,
    id: int,
    error_message: str = "Объект не найден"
) -> bool:
    """
    Проверяет существование объекта в базе данных
    """
    exists = db.query(model).filter(model.id == id).first() is not None
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_message
        )
    return True

def get_user_rating(
    db: Session,
    rating_model: Callable,
    user_id: int,
    item_id: int
) -> Optional[T]:
    """
    Получает рейтинг пользователя для конкретного объекта
    """
    return db.query(rating_model).filter(
        rating_model.user_id == user_id,
        rating_model.item_id == item_id
    ).first()

def check_owner_or_admin(
    current_user_id: int,
    owner_id: int,
    is_admin: bool = False,
    error_message: str = "Недостаточно прав для выполнения операции"
) -> None:
    """
    Проверяет, является ли текущий пользователь владельцем или администратором
    """
    if not (current_user_id == owner_id or is_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=error_message
        ) 