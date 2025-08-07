"""FastAPI application main module."""

import logging
import sys
from contextlib import asynccontextmanager

from api.endpoints import router
from core.config import settings
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager for startup and shutdown events.

    Args:
        app: The FastAPI application instance.
    """
    # Startup
    logger.info(f"Starting {settings.app_name} v{settings.version}")
    logger.info(f"Debug mode: {settings.debug}")
    yield
    # Shutdown
    logger.info(f"Shutting down {settings.app_name}")


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        The configured FastAPI application instance.
    """
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description="A production-ready API for managing users and their pets",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan
    )

    # Add security middleware
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["localhost", "127.0.0.1", "*.localhost"]
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=settings.allowed_methods,
        allow_headers=settings.allowed_headers,
    )

    # Include routers
    app.include_router(router)

    return app


# Create the application instance
app = create_application()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Custom exception handler for request validation errors.

    Args:
        request: The incoming request.
        exc: The validation error exception.

    Returns:
        A JSON response with error details.
    """
    logger.warning(f"Validation error on {request.url}: {exc}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": "Validation error",
            "detail": exc.errors()
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Custom exception handler for HTTP exceptions.

    Args:
        request: The incoming request.
        exc: The HTTP exception.

    Returns:
        A JSON response with error details.
    """
    logger.warning(f"HTTP error {exc.status_code} on {request.url}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.detail,
            "detail": getattr(exc, "detail", None)
        }
    )


@app.exception_handler(500)
async def internal_server_error_handler(request: Request, exc: Exception):
    """
    Custom exception handler for internal server errors.

    Args:
        request: The incoming request.
        exc: The exception that occurred.

    Returns:
        A JSON response with error details.
    """
    logger.error(f"Internal server error on {request.url}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "error": "Internal server error",
            "detail": "An unexpected error occurred"
        }
    )


@app.middleware("http")
async def add_correlation_id(request: Request, call_next):
    """
    Middleware to add correlation ID to logs for request tracing.

    Args:
        request: The incoming request.
        call_next: The next middleware or endpoint.

    Returns:
        The response from the next middleware or endpoint.
    """
    correlation_id = request.headers.get("X-Correlation-ID", "unknown")

    # Add correlation ID to logger context
    logger.info(
        f"Processing request {request.method} {request.url}",
        extra={"correlation_id": correlation_id}
    )

    response = await call_next(request)
    response.headers["X-Correlation-ID"] = correlation_id

    logger.info(
        f"Completed request {request.method} {request.url} with status {response.status_code}",
        extra={"correlation_id": correlation_id}
    )

    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        access_log=True
    )
