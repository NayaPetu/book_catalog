

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app.db.session import get_db
# from app.schemas import authors as schemas
# from app.crud import authors as crud_authors

# router = APIRouter()

# @router.post("/", response_model=schemas.AuthorResponse, status_code=201)
# def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
#     return crud_authors.create_author(db, author)

# @router.get("/", response_model=List[schemas.AuthorResponse])
# def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud_authors.get_authors(db, skip, limit)

# @router.get("/{author_id}", response_model=schemas.AuthorResponse)
# def read_author(author_id: int, db: Session = Depends(get_db)):
#     author = crud_authors.get_author(db, author_id)
#     if author is None:
#         raise HTTPException(status_code=404, detail="Author not found")
#     return author



from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.db.session import get_db
from app.schemas.authors import AuthorCreate, AuthorResponse
from app.crud.authors import create_author, get_author, get_authors

router = APIRouter()

@router.post("/", response_model=AuthorResponse, status_code=201)
def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)

@router.get("/", response_model=List[AuthorResponse])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_authors(db, skip, limit)

@router.get("/{author_id}", response_model=AuthorResponse)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author