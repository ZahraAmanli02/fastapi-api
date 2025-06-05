from pydantic import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./fastapi_app.db"
    JWT_SECRET_KEY: str = "supersecretkey123"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    MAX_POST_SIZE_BYTES: int = 1 * 1024 * 1024
    POSTS_CACHE_TTL_SECONDS: int = 5 * 60

    class Config:
        case_sensitive = True

settings = Settings()
