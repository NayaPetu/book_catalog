# from sqlalchemy import Column, Integer, String
# from app.db.base import Base

# class Author(Base):
#     __tablename__ = "authors"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     bio = Column(String, nullable=True)

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .books import Book

class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    bio: Optional[str] = None

    books: List["Book"] = Relationship(back_populates="author")