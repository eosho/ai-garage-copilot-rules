"""
Weather API main application module.

This module sets up the FastAPI application with all necessary middleware,
routing, and configuration for the weather API service.
"""

import logging
import sys
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import structlog
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.endpoints import router as weather_router
from core.config import get_settings
from core.logging_config import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan context manager.

    Handles startup and shutdown events for the FastAPI application.

    Args:
        app: The FastAPI application instance.

    Yields:
        None during the application's lifetime.
    """
    # Startup
    settings = get_settings()
    configure_logging(settings.log_level, settings.environment)

    logger = structlog.get_logger(__name__)
    logger.info(
        "Weather API starting up",
        version="0.1.0",
        environment=settings.environment,
        host=settings.host,
        port=settings.port
    )

    yield

    # Shutdown
    logger.info("Weather API shutting down")


# Create FastAPI application instance
app = FastAPI(
    title="Weather API",
    description="A production-ready weather API service with mock data",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def logging_middleware(request: Request, call_next) -> Response:
    """
    Request/response logging middleware.

    Logs all incoming requests and outgoing responses with timing information
    and correlation IDs for tracing.

    Args:
        request: The incoming HTTP request.
        call_next: The next middleware or endpoint handler.

    Returns:
        The HTTP response from the endpoint.
    """
    import time
    import uuid

    # Generate correlation ID for request tracing
    correlation_id = str(uuid.uuid4())

    # Bind correlation ID to logger context
    logger = structlog.get_logger(__name__).bind(correlation_id=correlation_id)

    start_time = time.perf_counter()

    # Log incoming request
    logger.info(
        "Request started",
        method=request.method,
        url=str(request.url),
        client_ip=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent"),
    )

    try:
        # Process request
        response = await call_next(request)

        # Calculate processing time
        process_time = time.perf_counter() - start_time

        # Add correlation ID to response headers
        response.headers["X-Correlation-ID"] = correlation_id
        response.headers["X-Process-Time"] = str(process_time)

        # Log response
        logger.info(
            "Request completed",
            status_code=response.status_code,
            process_time=process_time,
        )

        return response

    except Exception as e:
        # Calculate processing time for failed requests
        process_time = time.perf_counter() - start_time

        # Log error
        logger.error(
            "Request failed",
            error=str(e),
            process_time=process_time,
            exc_info=True,
        )

        # Return error response
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal server error",
                "correlation_id": correlation_id,
            },
            headers={"X-Correlation-ID": correlation_id},
        )


# Include routers
app.include_router(weather_router, prefix="/weather", tags=["weather"])


@app.get("/health", tags=["system"])
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns the current status of the API service for monitoring
    and load balancer health checks.

    Returns:
        Dictionary containing the service status and version.
    """
    return {
        "status": "healthy",
        "service": "weather-api",
        "version": "0.1.0",
    }


@app.get("/", tags=["system"])
async def root() -> dict[str, str]:
    """
    Root endpoint with API information.

    Returns:
        Dictionary containing basic API information and documentation links.
    """
    return {
        "service": "Weather API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn

    settings = get_settings()

    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.environment == "development",
        log_level=settings.log_level.lower(),
    )
