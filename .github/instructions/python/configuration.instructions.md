---
description: "Guidelines for managing configuration in Python applications."
applyTo: "**/*.py"
---

# Python Configuration Instructions

## General Principles

- **Environment Variables**: Use environment variables for configuration that varies between environments (e.g., database URLs, API keys).
- **Configuration Files**: Use a configuration file (e.g., `config.ini`, `settings.toml`) for non-sensitive, application-level settings.
- **Pydantic Settings**: Use Pydantic's `BaseSettings` to load and validate configuration from environment variables and files.
- **Centralized Access**: Provide a centralized way to access configuration settings throughout the application (e.g., a dependency injection system).

## Example

```python
# settings.py
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    """Application settings loaded from environment variables."""
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# main.py
from fastapi import FastAPI, Depends
from .settings import AppSettings

app = FastAPI()

def get_settings():
    return AppSettings()

@app.get("/info")
def get_app_info(settings: AppSettings = Depends(get_settings)):
    """Returns application information based on current settings."""
    return {"debug_mode": settings.DEBUG}
```
