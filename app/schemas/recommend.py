from pydantic import BaseModel
from typing import List
from .books import BookResponse

class RecommendationResponse(BaseModel):
    books: List[BookResponse]