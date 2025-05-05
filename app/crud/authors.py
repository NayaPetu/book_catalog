# from sqlalchemy.orm import Session
# from app.models import authors as models
# from app.schemas import authors as schemas

# def create_author(db: Session, author: schemas.AuthorCreate):
#     db_author = models.Author(**author.dict())
#     db.add(db_author)
#     db.commit()
#     db.refresh(db_author)
#     return db_author

# def get_author(db: Session, author_id: int):
#     return db.query(models.Author).filter(models.Author.id == author_id).first()

# def get_authors(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Author).offset(skip).limit(limit).all()


# from sqlmodel import Session, select
# from app.models.authors import Author
# from app.schemas.authors import AuthorCreate

# def create_author(db: Session, author: AuthorCreate):
#     db_author = Author(**author.dict())
#     db.add(db_author)
#     db.commit()
#     db.refresh(db_author)
#     return db_author

# def get_author(db: Session, author_id: int):
#     statement = select(Author).where(Author.id == author_id)
#     return db.exec(statement).first()

# def get_authors(db: Session, skip: int = 0, limit: int = 100):
#     statement = select(Author).offset(skip).limit(limit)
#     return db.exec(statement).all()


from sqlmodel import Session
from app.models.authors import Author
from app.schemas.authors import AuthorCreate
from app.crud.base import create_item, get_item, get_items

def create_author(db: Session, author: AuthorCreate):
    return create_item(db, Author(**author.dict()))

def get_author(db: Session, author_id: int):
    return get_item(db, Author, author_id)

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return get_items(db, Author, skip, limit)