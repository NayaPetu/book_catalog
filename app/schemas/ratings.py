"""Pydantic schemas for ratings."""

from pydantic import BaseModel


class RatingBase(BaseModel):
    """Base schema for ratings."""

    score: int
    book_id: int

    def get_score(self) -> int:
        """Return the rating's score."""
        return self.score


class RatingCreate(RatingBase):
    """Schema for creating a rating."""

    def validate_score(self) -> bool:
        """Validate the rating's score."""
        return 1 <= self.score <= 5


class RatingResponse(RatingBase):
    """Schema for rating response."""

    id: int
    user_id: int

    def get_id(self) -> int:
        """Return the rating's ID."""
        return self.id

    class Config:
        """Pydantic configuration."""
        from_attributes = True

# from pydantic import BaseModel

# class RatingBase(BaseModel):
#     score: int
#     book_id: int

# class RatingCreate(RatingBase):
#     pass

# class RatingResponse(RatingBase):
#     id: int
#     user_id: int

#     class Config:
#         from_attributes = True

