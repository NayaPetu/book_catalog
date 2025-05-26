"""Main entry point for the Book Catalog API."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users_router, authors_router, books_router, ratings_router, recommend_router
from app.db.database import create_tables

app = FastAPI(
    title="Book Catalog API",
    description="API для каталога книг с системой рейтингов и рекомендаций",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    """Создание таблиц при запуске приложения."""
    create_tables()

@app.get("/")
def read_root():
    """Return a welcome message for the API."""
    return {
        "message": "Welcome to the Book Catalog API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# Подключение роутеров
app.include_router(
    users_router,
    prefix="/api/users",
    tags=["Users"]
)
app.include_router(
    authors_router,
    prefix="/api/authors",
    tags=["Authors"]
)
app.include_router(
    books_router,
    prefix="/api/books",
    tags=["Books"]
)
app.include_router(
    ratings_router,
    prefix="/api/ratings",
    tags=["Ratings"]
)
app.include_router(
    recommend_router,
    prefix="/api/recommendations",
    tags=["Recommendations"]
)
