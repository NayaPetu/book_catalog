"""Main entry point for the Book Catalog API."""
from fastapi import FastAPI
from app.routers import users_router, authors_router, books_router, ratings_router, recommend_router


app = FastAPI(title="Book Catalog API")

@app.get("/")
def read_root():
    """Return a welcome message for the API."""
    return {"message": "Welcome to the Book Catalog API"}


app.include_router(users_router)
app.include_router(authors_router)
app.include_router(books_router)
app.include_router(ratings_router)
app.include_router(recommend_router)
