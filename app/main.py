from fastapi import FastAPI
from app.routers import users, authors, books, ratings, recommend
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="Book Catalog API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(ratings.router, prefix="/ratings", tags=["ratings"])
app.include_router(recommend.router, prefix="/recommend", tags=["recommend"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Catalog API"}