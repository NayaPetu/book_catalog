from pydantic import BaseModel

class RatingBase(BaseModel):
    score: int
    book_id: int

class RatingCreate(RatingBase):
    pass

class RatingResponse(RatingBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True