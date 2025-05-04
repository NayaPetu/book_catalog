from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author_id: int
    genre: Optional[str] = None
    publication_year: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookResponse(BookCreate):
    book_id: int
    class Config:
        from_attributes = True