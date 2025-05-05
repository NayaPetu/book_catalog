"""Tests for book endpoints."""

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.crud.authors import create_author
from app.crud.books import create_book
from app.schemas.authors import AuthorCreate
from app.schemas.books import BookCreate


def test_create_book(client: TestClient, db: Session):
    """Test creating a book."""
    author = AuthorCreate(name="Test Author")
    db_author = create_author(db, author)
    book = BookCreate(
        title="Test Book",
        author_id=db_author.id,
        genre="Fiction",
        publication_year=2023,
    )
    create_book(db, book)
    response = client.post(
        "/books/",
        json={
            "title": "Test Book 2",
            "author_id": db_author.id,
            "genre": "Non-Fiction",
            "publication_year": 2024,
        },
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book 2"


def test_read_books(client: TestClient, db: Session):
    """Test retrieving a list of books."""
    author = AuthorCreate(name="Test Author")
    db_author = create_author(db, author)
    book = BookCreate(title="Test Book", author_id=db_author.id)
    create_book(db, book)
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) > 0














# """Tests for book endpoints."""

# import pytest
# from fastapi.testclient import TestClient
# from sqlmodel import Session

# from app.crud.authors import create_author
# from app.schemas.authors import AuthorCreate


# def test_create_book(client: TestClient, db: Session):
#     """Test creating a book."""
#     author = AuthorCreate(name="Test Author")
#     db_author = create_author(db, author)
#     response = client.post(
#         "/books/",
#         json={"title": "Test Book", "author_id": db_author.id, "genre": "Fiction", "publication_year": 2023},
#     )
#     assert response.status_code == 201
#     assert response.json()["title"] == "Test Book"

# import pytest
# from fastapi.testclient import TestClient
# from app.main import app
# from sqlmodel import Session, SQLModel, create_engine
# from app.db.session import engine
# from app.crud.authors import create_author
# from app.schemas.authors import AuthorCreate

# client = TestClient(app)

# @pytest.fixture
# def db():
#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:
#         yield session
#     SQLModel.metadata.drop_all(engine)

# def test_create_book(db):
#     author = AuthorCreate(name="Test Author")
#     db_author = create_author(db, author)
#     response = client.post(
#         "/books/",
#         json={"title": "Test Book", "description": "Test Desc", "author_id": db_author.id}
#     )
#     assert response.status_code == 201
#     assert response.json()["title"] == "Test Book"