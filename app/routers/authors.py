"""Router for author-related endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud.authors import create_author, get_author, get_authors
from app.db.session import get_db
from app.schemas.authors import AuthorCreate, AuthorResponse


router = APIRouter()


@router.post("/", response_model=AuthorResponse, status_code=201)
def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_db)):
    """Create a new author."""
    return create_author(db, author)


@router.get("/", response_model=List[AuthorResponse])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a list of authors."""
    return get_authors(db, skip, limit)


@router.get("/{author_id}", response_model=AuthorResponse)
def read_author(author_id: int, db: Session = Depends(get_db)):
    """Retrieve an author by ID."""
    author = get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, author: AuthorCreate, db: Session = Depends(get_db)):
    """Update an author by ID."""
    db_author = get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    for key, value in author.dict().items():
        setattr(db_author, key, value)
    db.commit()
    db.refresh(db_author)
    return db_author


@router.delete("/{author_id}", status_code=204)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """Delete an author by ID."""
    db_author = get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(db_author)
    db.commit()