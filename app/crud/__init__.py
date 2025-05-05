"""Initialize CRUD module."""

from .authors import create_author, get_author, get_authors
from .books import create_book, get_book, get_books
from .ratings import create_rating, get_ratings_by_book
from .recommend import create_recommend, get_recommend
from .users import authenticate_user, create_access_token, create_user, get_user_by_username