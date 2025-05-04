from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.author_id"), nullable=False)
    genre = Column(String, nullable=True)
    publication_year = Column(Integer, nullable=True)
    isbn = Column(String, unique=True, nullable=True)