"""Tests for rating endpoints."""

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.crud.authors import create_author
from app.crud.books import create_book
from app.crud.ratings import create_rating
from app.crud.users import create_access_token, create_user
from app.schemas.authors import AuthorCreate
from app.schemas.books import BookCreate
from app.schemas.ratings import RatingCreate
from app.schemas.users import UserCreate


def test_create_rating(client: TestClient, db: Session):
    """Test creating a rating."""
    user = UserCreate(username="testuser", password="testpassword")
    db_user = create_user(db, user)
    author = AuthorCreate(name="Test Author")
    db_author = create_author(db, author)
    book = BookCreate(title="Test Book", author_id=db_author.id)
    db_book = create_book(db, book)
    rating = RatingCreate(score=5, book_id=db_book.id)
    create_rating(db, rating, db_user.id)
    token = create_access_token({"sub": db_user.username})
    response = client.post(
        "/ratings/",
        json={"score": 4, "book_id": db_book.id},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    assert response.json()["score"] == 4


def test_create_rating_unauthorized(client: TestClient, db: Session):
    """Test creating a rating without authorization."""
    author = AuthorCreate(name="Test Author")
    db_author = create_author(db, author)
    book = BookCreate(title="Test Book", author_id=db_author.id)
    db_book = create_book(db, book)
    response = client.post("/ratings/", json={"score": 5, "book_id": db_book.id})
    assert response.status_code == 401













# """Tests for rating endpoints."""

# import pytest
# from fastapi.testclient import TestClient
# from sqlmodel import Session

# from app.crud.books import create_book
# from app.crud.users import create_access_token, create_user
# from app.schemas.books import BookCreate
# from app.schemas.users import UserCreate


# def test_create_rating(client: TestClient, db: Session):
#     """Test creating a rating."""
#     user = UserCreate(username="testuser", password="testpassword")
#     db_user = create_user(db, user)
#     book = BookCreate(title="Test Book", author_id=1, genre="Fiction", publication_year=2023)
#     db_book = create_book(db, book)
#     token = create_access_token({"sub": db_user.username})
#     response = client.post(
#         "/ratings/",
#         json={"score": 5, "book_id": db_book.id},
#         headers={"Authorization": f"Bearer {token}"},
#     )
#     assert response.status_code == 201
#     assert response.json()["score"] == 5


# def test_create_rating_unauthorized(client: TestClient, db: Session):
#     """Test creating a rating without authorization."""
#     response = client.post("/ratings/", json={"score": 5, "book_id": 1})
#     assert response.status_code == 401



# import pytest
# from fastapi.testclient import TestClient
# from app.main import app
# from sqlmodel import Session, SQLModel, create_engine
# from app.db.session import engine
# from app.crud.users import create_user, create_access_token
# from app.schemas.users import UserCreate

# client = TestClient(app)

# @pytest.fixture
# def db():
#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:
#         yield session
#     SQLModel.metadata.drop_all(engine)

# def test_create_rating(db):
#     user = UserCreate(username="testuser", password="testpassword")
#     db_user = create_user(db, user)
#     token = create_access_token({"sub": db_user.username})
#     response = client.post(
#         "/ratings/",
#         json={"score": 5, "book_id": 1},
#         headers={"Authorization": f"Bearer {token}"}
#     )
#     assert response.status_code == 201
#     assert response.json()["score"] == 5