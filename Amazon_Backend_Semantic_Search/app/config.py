"""
Centralized application configuration.
All environment-driven settings live here so nothing is hardcoded
across the codebase.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- App ---
    APP_NAME: str = "Amazon-Backend"
    ENV: str = "development"

    # --- Database ---
    # Swap this single URL to switch from SQLite -> PostgreSQL/MySQL.
    # e.g. postgresql://user:password@localhost:5432/amazon_db
    # e.g. mysql+pymysql://user:password@localhost:3306/amazon_db
    DATABASE_URL: str = "sqlite:///./amazon.db"

    # --- Auth / JWT ---
    SECRET_KEY: str = "CHANGE_ME_IN_PRODUCTION_9f8a7d6c5b4e3f2a1"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # --- Logging ---
    LOG_DIR: str = "logs"
    LOG_FILE: str = "app.log"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
