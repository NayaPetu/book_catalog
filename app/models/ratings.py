# from sqlalchemy import Column, Integer, ForeignKey
# from app.db.base import Base

# class Rating(Base):
#     __tablename__ = "ratings"

#     id = Column(Integer, primary_key=True, index=True)
#     score = Column(Integer)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     book_id = Column(Integer, ForeignKey("books.id"))

from sqlmodel import SQLModel, Field
from typing import Optional

class Rating(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    score: int
    user_id: int = Field(foreign_key="user.id")
    book_id: int = Field(foreign_key="book.id")