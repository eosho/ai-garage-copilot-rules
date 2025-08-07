# Users & Pets FastAPI Application

A production-ready FastAPI application that provides an API for managing users and their pets. Built with security, scalability, and maintainability in mind.

## 🚀 Features

- **RESTful API** for users and pets management
- **Production-ready** with comprehensive error handling and logging
- **Security-first** approach with JWT authentication support
- **Comprehensive documentation** with OpenAPI/Swagger
- **Docker containerization** with multi-stage builds
- **Health checks** and monitoring endpoints
- **CORS configuration** for frontend integration
- **Extensive testing** with pytest (>80% coverage)
- **Type hints** throughout the codebase
- **Structured logging** with correlation IDs

## 📋 API Endpoints

### Core Endpoints
- `GET /api/v1/users` - List all users with their pets
- `GET /api/v1/users/{user_id}` - Get specific user with pets
- `GET /api/v1/users/stats/pet-count` - Get user and pet statistics
- `GET /api/v1/health` - Health check endpoint

### Query Parameters
- `GET /api/v1/users?species=dog` - Filter users by pet species

### Documentation
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## 🛠️ Technology Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server for running the application
- **Python 3.11** - Latest stable Python version
- **Docker** - Containerization and deployment
- **pytest** - Testing framework with comprehensive coverage

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip
- Docker (optional, for containerized deployment)

### Local Development

1. **Clone and setup**:
   ```bash
   cd example
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**:
   ```bash
   python -m app.main
   ```

6. **Access the API**:
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Health check: http://localhost:8000/api/v1/health

### Docker Deployment

1. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

2. **Run in production mode** (with nginx):
   ```bash
   docker-compose --profile production up --build
   ```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_endpoints.py

# Run with verbose output
pytest -v
```

## 🔒 Security Features

- **Input validation** with Pydantic models
- **CORS configuration** for cross-origin requests
- **Trusted host middleware** for host validation
- **JWT token support** (infrastructure ready)
- **Non-root Docker user** for container security
- **Structured error handling** without sensitive data exposure

## 📊 Sample Data

The application includes mock data with:
- 5 users with various pet configurations
- Different pet species (dogs, cats, birds, fish)
- Users with multiple pets and users with no pets
- Realistic user profiles with timestamps

### Example User Response:
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Alice Johnson",
      "email": "alice.johnson@example.com",
      "age": 28,
      "pets": [
        {
          "id": 1,
          "name": "Buddy",
          "species": "dog",
          "breed": "Golden Retriever",
          "age": 3
        }
      ],
      "created_at": "2023-01-15T10:30:00"
    }
  ],
  "message": "Successfully retrieved all users"
}
```

## 🏗️ Architecture

### Project Structure
```
app/
├── __init__.py              # Package initialization
├── main.py                  # FastAPI application and configuration
├── api/
│   ├── __init__.py
│   └── endpoints.py         # API route definitions
├── core/
│   ├── __init__.py
│   ├── config.py           # Application configuration
│   └── security.py         # Security utilities
├── models/
│   ├── __init__.py
│   └── schemas.py          # Pydantic models
└── services/
    ├── __init__.py
    └── user_service.py     # Business logic
```

### Key Components

- **FastAPI Application**: Main app with middleware, error handlers, and CORS
- **Pydantic Models**: Type-safe request/response schemas
- **Service Layer**: Business logic separation from API endpoints
- **Configuration Management**: Environment-based settings with Pydantic
- **Error Handling**: Custom exception handlers with proper HTTP status codes
- **Logging**: Structured logging with correlation IDs

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Enable debug mode | `false` |
| `SECRET_KEY` | JWT secret key | Required in production |
| `ALLOWED_ORIGINS` | CORS allowed origins | localhost URLs |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration | `30` |

### Production Considerations

1. **Set a strong SECRET_KEY** for JWT tokens
2. **Configure proper ALLOWED_ORIGINS** for CORS
3. **Set DEBUG=false** in production
4. **Use HTTPS** in production environments
5. **Configure proper logging** destinations
6. **Set up monitoring** and alerting

## 📈 Monitoring and Observability

### Health Checks
- Container health checks via `/api/v1/health`
- Docker Compose health check configuration
- Kubernetes readiness/liveness probe ready

### Logging
- Structured JSON logging
- Correlation ID tracking for requests
- Error logging with stack traces
- Access logging for all requests

### Metrics Ready
The application is designed to easily integrate with:
- Prometheus metrics collection
- Grafana dashboards
- APM tools (New Relic, DataDog, etc.)

## 🤝 Contributing

1. Follow the coding standards in `.github/copilot-instructions.md`
2. Write tests for new features
3. Ensure >80% test coverage
4. Use type hints throughout
5. Follow security best practices

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the API documentation at `/docs`
- Review the health check endpoint at `/api/v1/health`
- Check application logs for error details
