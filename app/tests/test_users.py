import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import Session, SQLModel, create_engine
from app.db.session import engine
from app.crud.users import create_user, create_access_token
from app.schemas.users import UserCreate

client = TestClient(app)

@pytest.fixture
def db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

def test_register_user(db):
    response = client.post(
        "/users/register",
        json={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_login_user(db):
    user = UserCreate(username="testuser2", password="testpassword")
    create_user(db, user)
    response = client.post(
        "/users/login",
        data={"username": "testuser2", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()