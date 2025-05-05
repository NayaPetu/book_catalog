"""Configuration module for the Book Catalog API."""

from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration settings loaded from environment variables."""

    database_url: str = Field(..., env="DATABASE_URL")
    secret_key: Optional[str] = Field(None, env="SECRET_KEY")
    algorithm: Optional[str] = Field("HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    db_user: Optional[str] = Field(None, env="DB_USER")
    db_password: Optional[str] = Field(None, env="DB_PASSWORD")
    db_name: Optional[str] = Field(None, env="DB_NAME")
    db_host: Optional[str] = Field(None, env="DB_HOST")
    db_port: Optional[str] = Field(None, env="DB_PORT")

    class Config:
        """Pydantic configuration for loading environment variables."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

    def get_db_url(self) -> str:
        """Return the database URL."""
        return self.database_url

    def get_token_expiry(self) -> int:
        """Return the token expiry duration in minutes."""
        return self.access_token_expire_minutes


settings = Settings()


# """Configuration module for the Book Catalog API."""

# from typing import Optional

# from pydantic import Field
# from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     """Application configuration settings loaded from environment variables."""

#     database_url: str = Field(..., env="DATABASE_URL")
#     secret_key: Optional[str] = Field(None, env="SECRET_KEY")
#     algorithm: Optional[str] = Field("HS256", env="ALGORITHM")
#     access_token_expire_minutes: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
#     db_user: Optional[str] = Field(None, env="DB_USER")
#     db_password: Optional[str] = Field(None, env="DB_PASSWORD")
#     db_name: Optional[str] = Field(None, env="DB_NAME")
#     db_host: Optional[str] = Field(None, env="DB_HOST")
#     db_port: Optional[str] = Field(None, env="DB_PORT")

#     class Config:
#         """Pydantic configuration for loading environment variables."""

#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         extra = "ignore"


# settings = Settings()