"""
Application configuration management.

This module provides centralized configuration management using Pydantic Settings
for environment variable loading and validation.
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    This class defines all configurable settings for the weather API service,
    with sensible defaults and environment variable loading.
    """
    
    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Application configuration
    environment: Literal["development", "staging", "production"] = "development"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    
    # API configuration
    api_title: str = "Weather API"
    api_description: str = "A production-ready weather API service with mock data"
    api_version: str = "0.1.0"
    
    # CORS configuration
    cors_origins: list[str] = ["*"]
    cors_methods: list[str] = ["*"]
    cors_headers: list[str] = ["*"]
    
    # Rate limiting (for future implementation)
    rate_limit_requests_per_minute: int = 100
    
    # Mock data configuration
    enable_mock_data: bool = True
    mock_response_delay_ms: int = 0  # Simulate API latency
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "WEATHER_API_"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached application settings.
    
    This function returns a cached instance of the Settings class,
    ensuring that environment variables are only read once during
    the application lifecycle.
    
    Returns:
        Cached Settings instance with loaded configuration.
    """
    return Settings()
