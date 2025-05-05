"""Pydantic schemas for users."""

from pydantic import BaseModel


class UserBase(BaseModel):
    """Base schema for users."""

    username: str

    def get_username(self) -> str:
        """Return the user's username."""
        return self.username


class UserCreate(UserBase):
    """Schema for creating a user."""

    password: str

    def validate_username(self) -> bool:
        """Validate the user's username."""
        return len(self.username) > 0


class UserResponse(UserBase):
    """Schema for user response."""

    id: int

    def get_id(self) -> int:
        """Return the user's ID."""
        return self.id

    class Config:
        """Pydantic configuration."""
        from_attributes = True