from pydantic import BaseModel
from typing import List
from .books import BookResponse

class RecommendCreate(BaseModel):
    book_id: int

class RecommendationResponse(BaseModel):
    books: List[BookResponse]