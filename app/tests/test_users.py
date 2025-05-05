"""Tests for user endpoints."""

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.crud.users import create_user
from app.schemas.users import UserCreate


def test_register_user(client: TestClient, db: Session):
    """Test registering a new user."""
    user = UserCreate(username="testuser", password="testpassword")
    create_user(db, user)
    response = client.post(
        "/users/register",
        json={"username": "testuser2", "password": "testpassword"},
    )
    assert response.status_code == 201
    assert response.json()["username"] == "testuser2"


def test_login_user(client: TestClient, db: Session):
    """Test user login."""
    user = UserCreate(username="testuser", password="testpassword")
    create_user(db, user)
    response = client.post(
        "/users/login",
        data={"username": "testuser", "password": "testpassword"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_read_user_me(client: TestClient, db: Session):
    """Test retrieving current user information."""
    user = UserCreate(username="testuser", password="testpassword")
    db_user = create_user(db, user)
    token = create_access_token({"sub": db_user.username})
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"










# """Tests for user endpoints."""

# import pytest
# from fastapi.testclient import TestClient
# from sqlmodel import Session

# from app.crud.users import create_user
# from app.schemas.users import UserCreate


# def test_register_user(client: TestClient, db: Session):
#     """Test registering a new user."""
#     response = client.post(
#         "/users/register",
#         json={"username": "testuser", "password": "testpassword"},
#     )
#     assert response.status_code == 201
#     assert response.json()["username"] == "testuser"


# def test_login_user(client: TestClient, db: Session):
#     """Test user login."""
#     user = UserCreate(username="testuser2", password="testpassword")
#     create_user(db, user)
#     response = client.post(
#         "/users/login",
#         data={"username": "testuser2", "password": "testpassword"},
#     )
#     assert response.status_code == 200
#     assert "access_token" in response.json()



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

# def test_register_user(db):
#     response = client.post(
#         "/users/register",
#         json={"username": "testuser", "password": "testpassword"}
#     )
#     assert response.status_code == 201
#     assert response.json()["username"] == "testuser"

# def test_login_user(db):
#     user = UserCreate(username="testuser2", password="testpassword")
#     create_user(db, user)
#     response = client.post(
#         "/users/login",
#         data={"username": "testuser2", "password": "testpassword"}
#     )
#     assert response.status_code == 200
#     assert "access_token" in response.json()