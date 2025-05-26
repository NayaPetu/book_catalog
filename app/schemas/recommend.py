"""Pydantic models for recommendations."""
from pydantic import BaseModel, Field
from typing import List
from .books import BookResponse

class RecommendBase(BaseModel):
    """Base recommendation schema."""
    user_id: int
    book_id: int
    score: float = Field(..., ge=0, le=5, description="Рейтинг от 0 до 5")

class RecommendCreate(RecommendBase):
    """Schema for creating a recommendation."""
    pass

class RecommendUpdate(BaseModel):
    """Schema for updating a recommendation."""
    score: float = Field(..., ge=0, le=5, description="Рейтинг от 0 до 5")

class Recommend(RecommendBase):
    """Schema for a recommendation in response."""
    id: int

    class Config:
        """Pydantic configuration."""
        from_attributes = True

class RecommendationResponse(BaseModel):
    books: List[BookResponse]