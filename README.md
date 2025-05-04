Book Catalog API
A RESTful API for managing a book catalog, built with FastAPI and PostgreSQL.
Features

CRUD operations for books, authors, and ratings.
User authentication with JWT.
Book recommendation system based on user preferences.
Automated tests with >70% coverage.
Database migrations with Alembic.

Setup

Clone the repository:git clone <repository-url>
cd project


Create a .env file based on .env.example.
Install dependencies:pip install -r requirements.txt


Start the application with Docker Compose:docker-compose up --build


Apply database migrations:alembic upgrade head



Usage

Access the API at http://localhost:8000.
Use the interactive API docs at http://localhost:8000/docs.

Running Tests
pytest

