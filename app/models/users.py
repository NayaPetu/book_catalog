"""User model definition."""

from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """User database model."""

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str