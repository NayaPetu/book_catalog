"""Pydantic schemas for authors."""

from typing import Optional

from pydantic import BaseModel


class AuthorBase(BaseModel):
    """Base schema for authors."""

    name: str
    bio: Optional[str] = None

    def get_name(self) -> str:
        """Return the author's name."""
        return self.name


class AuthorCreate(AuthorBase):
    """Schema for creating an author."""

    def validate_name(self) -> bool:
        """Validate the author's name."""
        return len(self.name) > 0


class AuthorResponse(AuthorBase):
    """Schema for author response."""

    id: int

    def get_id(self) -> int:
        """Return the author's ID."""
        return self.id

    class Config:
        """Pydantic configuration."""
        from_attributes = True

# from pydantic import BaseModel
# from typing import Optional

# class AuthorBase(BaseModel):
#     name: str
#     bio: Optional[str] = None

# class AuthorCreate(AuthorBase):
#     pass

# class AuthorResponse(AuthorBase):
#     id: int

#     class Config:
#         from_attributes = True