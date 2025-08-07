"""
Logging configuration for the weather API service.

This module provides structured logging configuration using structlog
for consistent and searchable log output across the application.
"""

import logging
import sys
from typing import Any, Dict, Literal

import structlog


def configure_logging(
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    environment: Literal["development", "staging", "production"],
) -> None:
    """
    Configure structured logging for the application.
    
    Sets up structlog with appropriate processors and formatters
    based on the environment and log level.
    
    Args:
        log_level: The minimum log level to output.
        environment: The current environment (affects log formatting).
    """
    # Configure stdlib logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper()),
    )
    
    # Configure structlog processors
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
    ]
    
    if environment == "development":
        # Pretty printing for development
        processors.append(structlog.dev.ConsoleRenderer(colors=True))
    else:
        # JSON output for production
        processors.append(structlog.processors.JSONRenderer())
    
    # Configure structlog
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, log_level.upper())
        ),
        logger_factory=structlog.WriteLoggerFactory(),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str) -> structlog.BoundLogger:
    """
    Get a configured logger instance.
    
    Args:
        name: The logger name (typically __name__).
        
    Returns:
        Configured structlog logger instance.
    """
    return structlog.get_logger(name)
