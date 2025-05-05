"""Author model definition."""

from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    """Author database model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    bio: Optional[str] = None

    books: List["Book"] = Relationship(back_populates="author")