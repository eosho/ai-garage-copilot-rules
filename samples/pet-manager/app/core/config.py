"""Core configuration and settings for the FastAPI application."""

from typing import List

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "Users & Pets API"
    version: str = "1.0.0"
    debug: bool = False

    # Security settings
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS settings
    allowed_origins: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    allowed_methods: List[str] = ["GET", "POST", "PUT", "DELETE"]
    allowed_headers: List[str] = ["*"]

    # API settings
    api_v1_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = AppSettings()
