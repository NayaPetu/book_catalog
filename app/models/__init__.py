"""Initialize models module."""

from .base import Base, BaseModel
from .users import User
from .books import Book
from .authors import Author
from .ratings import Rating
from .recommend import Recommendation

__all__ = [
    'Base',
    'BaseModel',
    'User',
    'Book',
    'Author',
    'Rating',
    'Recommendation'
]