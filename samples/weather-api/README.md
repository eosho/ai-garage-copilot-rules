# Weather API Service

A production-ready weather API service built with FastAPI, featuring mock data for demonstration purposes.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Pydantic Models**: Data validation and serialization
- **Structured Logging**: Comprehensive logging with correlation IDs
- **Security**: Input validation and error handling
- **Docker Support**: Containerized deployment
- **Test Coverage**: Comprehensive test suite
- **Documentation**: Auto-generated OpenAPI documentation

## API Endpoints

- `GET /weather/current/{city}` - Get current weather for a city
- `GET /weather/forecast/{city}` - Get weather forecast for a city
- `GET /weather/cities` - Get list of supported cities
- `GET /health` - Health check endpoint

## Quick Start

### Using UV (Recommended)

```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Run the development server
uv run uvicorn weather_api.main:app --reload --host 0.0.0.0 --port 8000
```

### Using Docker

```bash
# Build the Docker image
docker build -t weather-api .

# Run the container
docker run -p 8000:8000 weather-api
```

## API Documentation

Once the service is running, visit:
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

## Testing

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=weather_api --cov-report=html
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `WEATHER_API_HOST` | Host to bind the server | `0.0.0.0` |
| `WEATHER_API_PORT` | Port to bind the server | `8000` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `ENVIRONMENT` | Environment name | `development` |

## Architecture

The service follows Clean Architecture principles:

- **`main.py`**: Application entry point and FastAPI setup
- **`api/`**: API endpoints and routing
- **`core/`**: Core business logic and configuration
- **`models/`**: Pydantic models and schemas
- **`services/`**: Business logic and data services
- **`data/`**: Mock data and data providers

## Security Features

- Input validation on all endpoints
- Comprehensive error handling
- Request/response logging
- Rate limiting ready (configurable)
- CORS support

## Deployment

The service is ready for deployment to:
- **Azure Container Apps**
- **Azure App Service**
- **Docker containers**
- **Kubernetes clusters**
