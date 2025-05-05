import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import Session, SQLModel, create_engine
from app.db.session import engine

client = TestClient(app)

@pytest.fixture
def db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

def test_create_author():
    response = client.post(
        "/authors/",
        json={"name": "Test Author", "bio": "Test Bio"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Author"

def test_read_authors():
    response = client.get("/authors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_author(db):
    response = client.post(
        "/authors/",
        json={"name": "Test Author", "bio": "Test Bio"}
    )
    author_id = response.json()["id"]
    response = client.put(
        f"/authors/{author_id}",
        json={"name": "Updated Author", "bio": "Updated Bio"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Author"

def test_delete_author(db):
    response = client.post(
        "/authors/",
        json={"name": "Test Author", "bio": "Test Bio"}
    )
    author_id = response.json()["id"]
    response = client.delete(f"/authors/{author_id}")
    assert response.status_code == 204
    response = client.get(f"/authors/{author_id}")
    assert response.status_code == 404