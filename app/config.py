# # Чтение переменных окружения из .env.

# from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     database_url: str
#     secret_key: str
#     algorithm: str = "HS256"

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"

# settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Игнорировать лишние поля, если они есть

settings = Settings()