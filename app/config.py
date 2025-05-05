# # Чтение переменных окружения из .env.

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
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
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()



# from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     database_url: str
#     secret_key: str
#     algorithm: str = "HS256"

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"

# settings = Settings()

# from pydantic_settings import BaseSettings
# from pydantic import Field
# from typing import Optional

# class Settings(BaseSettings):
#     database_url: str = Field(..., env="DATABASE_URL")
#     secret_key: Optional[str] = Field(None, env="SECRET_KEY")
#     algorithm: Optional[str] = Field("HS256", env="ALGORITHM")
#     db_user: Optional[str] = Field(None, env="DB_USER")
#     db_password: Optional[str] = Field(None, env="DB_PASSWORD")
#     db_name: Optional[str] = Field(None, env="DB_NAME")
#     db_host: Optional[str] = Field(None, env="DB_HOST")
#     db_port: Optional[str] = Field(None, env="DB_PORT")
    
#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         extra = "ignore"  # Игнорировать лишние поля, если они есть

# settings = Settings()


# from pydantic_settings import BaseSettings
# from dotenv import load_dotenv

# load_dotenv()

# class Settings(BaseSettings):
#     database_url: str
#     secret_key: str
#     algorithm: str

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         extra = "ignore"

# settings = Settings()