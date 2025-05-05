"""Tests for recommendation endpoints."""

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.crud.users import create_access_token, create_user
from app.schemas.users import UserCreate


def test_recommendations(client: TestClient, db: Session):
    """Test retrieving book recommendations."""
    user = UserCreate(username="testuser", password="testpassword")
    db_user = create_user(db, user)
    token = create_access_token({"sub": db_user.username})
    response = client.get("/recommend/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "books" in response.json()










# """Tests for recommendation endpoints."""

# import pytest
# from fastapi.testclient import TestClient
# from sqlmodel import Session

# from app.crud.users import create_access_token, create_user
# from app.schemas.users import UserCreate


# def test_recommendations(client: TestClient, db: Session):
#     """Test retrieving book recommendations."""
#     user = UserCreate(username="testuser", password="testpassword")
#     db_user = create_user(db, user)
#     token = create_access_token({"sub": db_user.username})
#     response = client.get("/recommend/", headers={"Authorization": f"Bearer {token}"})
#     assert response.status_code == 200
#     assert "books" in response.json()



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

# def test_recommendations(db):
#     user = UserCreate(username="testuser", password="testpassword")
#     db_user = create_user(db, user)
#     token = create_access_token({"sub": db_user.username})
#     response = client.get(
#         "/recommend/",
#         headers={"Authorization": f"Bearer {token}"}
#     )
#     assert response.status_code == 200
#     assert "books" in response.json()