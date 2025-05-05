from sqlmodel import Session, SQLModel, select
from typing import TypeVar, Type, Optional, List

T = TypeVar("T", bound=SQLModel)

def create_item(db: Session, item: T) -> T:
    db_item = item.__class__(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, model: Type[T], item_id: int) -> Optional[T]:
    statement = select(model).where(model.id == item_id)
    return db.exec(statement).first()

def get_items(db: Session, model: Type[T], skip: int = 0, limit: int = 100) -> List[T]:
    statement = select(model).offset(skip).limit(limit)
    return db.exec(statement).all()

def update_item(db: Session, model: Type[T], item_id: int, item_data: dict) -> Optional[T]:
    db_item = get_item(db, model, item_id)
    if db_item is None:
        return None
    for key, value in item_data.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, model: Type[T], item_id: int) -> bool:
    db_item = get_item(db, model, item_id)
    if db_item is None:
        return False
    db.delete(db_item)
    db.commit()
    return True