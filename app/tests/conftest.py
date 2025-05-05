"""Common test fixtures."""

from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel

from app.db.session import engine
from app.main import app


def client():
    """Provide a test client for the application."""
    return TestClient(app)


def db():
    """Provide a test database session."""
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

# """Common test fixtures."""

# import pytest
# from fastapi.testclient import TestClient
# from sqlmodel import Session, SQLModel

# from app.db.session import engine
# from app.main import app


# @pytest.fixture
# def client():
#     """Provide a test client for the application."""
#     return TestClient(app)


# @pytest.fixture
# def db():
#     """Provide a test database session."""
#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:
#         yield session
#     SQLModel.metadata.drop_all(engine)