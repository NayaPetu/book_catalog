# from sqlalchemy import Column, Integer, String, ForeignKey
# from app.db.base import Base

# class Book(Base):
#     __tablename__ = "books"
#     book_id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     author_id = Column(Integer, ForeignKey("authors.author_id"), nullable=False)
#     genre = Column(String, nullable=True)
#     publication_year = Column(Integer, nullable=True)
#     isbn = Column(String, unique=True, nullable=True)

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.db.base import Base

# class Book(Base):
#     __tablename__ = "books"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     genre = Column(String, nullable=True)
#     publication_year = Column(Integer, nullable=True)
#     author_id = Column(Integer, ForeignKey("authors.id"))

#     author = relationship("Author", back_populates="books")

# Author.books = relationship("Book", back_populates="author")


# from sqlmodel import SQLModel, Field, Relationship
# from typing import Optional

# class Book(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     title: str = Field(index=True)
#     description: Optional[str] = None
#     author_id: int = Field(foreign_key="author.id")

#     author: Optional["Author"] = Relationship(back_populates="books")

# class Author(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     bio: Optional[str] = None

#     books: list["Book"] = Relationship(back_populates="author")



from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    genre: Optional[str] = None
    publication_year: Optional[str] = None
    author_id: int = Field(foreign_key="author.id")

    author: Optional["Author"] = Relationship(back_populates="books")