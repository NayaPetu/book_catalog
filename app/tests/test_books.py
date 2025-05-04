import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import Session, SQLModel, create_engine
from app.db.session import engine
from app.crud.authors import create_author
from app.schemas.authors import AuthorCreate

client = TestClient(app)

@pytest.fixture
def db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

def test_create_book(db):
    author = AuthorCreate(name="Test Author")
    db_author = create_author(db, author)
    response = client.post(
        "/books/",
        json={"title": "Test Book", "description": "Test Desc", "author_id": db_author.id}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"