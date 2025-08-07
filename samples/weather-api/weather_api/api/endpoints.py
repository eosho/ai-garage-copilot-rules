"""
Weather API endpoints.

This module defines all the REST API endpoints for the weather service,
including current weather, forecasts, and city management.
"""

from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse

from core.logging_config import get_logger
from models.schemas import (
    CurrentWeather,
    ErrorResponse,
    SupportedCitiesResponse,
    SupportedCity,
    WeatherForecast,
)
from services.weather_service import weather_service

# Create API router
router = APIRouter()
logger = get_logger(__name__)


@router.get(
    "/current/{city}",
    response_model=CurrentWeather,
    responses={
        404: {"model": ErrorResponse, "description": "City not found"},
        422: {"model": ErrorResponse, "description": "Invalid city name"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    summary="Get current weather",
    description="Retrieve current weather conditions for a specified city",
)
async def get_current_weather(
    city: str = Path(
        ...,
        description="Name of the city to get weather for",
        min_length=1,
        max_length=100,
        example="london"
    )
) -> CurrentWeather:
    """
    Get current weather conditions for a specified city.

    This endpoint returns comprehensive current weather data including
    temperature, humidity, wind conditions, and weather description.

    Args:
        city: Name of the city (case-insensitive).

    Returns:
        Current weather data for the specified city.

    Raises:
        HTTPException: 404 if city is not supported, 422 if city name is invalid.
    """
    try:
        # Validate input
        if not city or not city.strip():
            raise HTTPException(
                status_code=422,
                detail={
                    "error": "Invalid city name",
                    "error_code": "INVALID_CITY_NAME",
                    "details": {"message": "City name cannot be empty"}
                }
            )

        # Get weather data
        weather_data = await weather_service.get_current_weather(city)

        if not weather_data:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": f"City '{city}' not found",
                    "error_code": "CITY_NOT_FOUND",
                    "details": {
                        "city": city,
                        "message": "The specified city is not supported. Use /weather/cities to see available cities."
                    }
                }
            )

        return weather_data

    except HTTPException:
        raise
    except ValueError as e:
        logger.warning(
            "Invalid input for current weather",
            city=city,
            error=str(e)
        )
        raise HTTPException(
            status_code=422,
            detail={
                "error": "Invalid input",
                "error_code": "VALIDATION_ERROR",
                "details": {"message": str(e)}
            }
        )
    except Exception as e:
        logger.error(
            "Failed to get current weather",
            city=city,
            error=str(e),
            exc_info=True
        )
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal server error",
                "error_code": "INTERNAL_ERROR",
                "details": {"message": "An unexpected error occurred"}
            }
        )


@router.get(
    "/forecast/{city}",
    response_model=WeatherForecast,
    responses={
        404: {"model": ErrorResponse, "description": "City not found"},
        422: {"model": ErrorResponse, "description": "Invalid parameters"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    summary="Get weather forecast",
    description="Retrieve multi-day weather forecast for a specified city",
)
async def get_weather_forecast(
    city: str = Path(
        ...,
        description="Name of the city to get forecast for",
        min_length=1,
        max_length=100,
        example="tokyo"
    ),
    days: int = Query(
        default=5,
        ge=1,
        le=10,
        description="Number of forecast days (1-10)",
        example=5
    )
) -> WeatherForecast:
    """
    Get weather forecast for a specified city.

    This endpoint returns detailed weather forecast data for up to 10 days,
    including daily high/low temperatures, precipitation, and conditions.

    Args:
        city: Name of the city (case-insensitive).
        days: Number of forecast days (1-10, default 5).

    Returns:
        Weather forecast data for the specified city and period.

    Raises:
        HTTPException: 404 if city is not supported, 422 if parameters are invalid.
    """
    try:
        # Validate input
        if not city or not city.strip():
            raise HTTPException(
                status_code=422,
                detail={
                    "error": "Invalid city name",
                    "error_code": "INVALID_CITY_NAME",
                    "details": {"message": "City name cannot be empty"}
                }
            )

        # Get forecast data
        forecast_data = await weather_service.get_weather_forecast(city, days)

        if not forecast_data:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": f"City '{city}' not found",
                    "error_code": "CITY_NOT_FOUND",
                    "details": {
                        "city": city,
                        "message": "The specified city is not supported. Use /weather/cities to see available cities."
                    }
                }
            )

        return forecast_data

    except HTTPException:
        raise
    except ValueError as e:
        logger.warning(
            "Invalid input for weather forecast",
            city=city,
            days=days,
            error=str(e)
        )
        raise HTTPException(
            status_code=422,
            detail={
                "error": "Invalid input",
                "error_code": "VALIDATION_ERROR",
                "details": {"message": str(e)}
            }
        )
    except Exception as e:
        logger.error(
            "Failed to get weather forecast",
            city=city,
            days=days,
            error=str(e),
            exc_info=True
        )
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal server error",
                "error_code": "INTERNAL_ERROR",
                "details": {"message": "An unexpected error occurred"}
            }
        )


@router.get(
    "/cities",
    response_model=SupportedCitiesResponse,
    responses={
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    summary="Get supported cities",
    description="Retrieve list of all cities supported by the weather API",
)
async def get_supported_cities(
    search: Optional[str] = Query(
        None,
        description="Search query to filter cities",
        min_length=1,
        max_length=50,
        example="new"
    )
) -> SupportedCitiesResponse:
    """
    Get list of all supported cities.

    This endpoint returns information about all cities that are supported
    by the weather API, including their coordinates and timezone data.

    Args:
        search: Optional search query to filter cities by name, country, or region.

    Returns:
        List of supported cities with their details.

    Raises:
        HTTPException: 500 if an internal error occurs.
    """
    try:
        if search:
            # Search for cities matching the query
            cities = await weather_service.search_cities(search)
            return SupportedCitiesResponse(
                cities=cities,
                total_count=len(cities)
            )
        else:
            # Get all supported cities
            return await weather_service.get_supported_cities()

    except Exception as e:
        logger.error(
            "Failed to get supported cities",
            search=search,
            error=str(e),
            exc_info=True
        )
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal server error",
                "error_code": "INTERNAL_ERROR",
                "details": {"message": "An unexpected error occurred"}
            }
        )


@router.get(
    "/cities/{city}/validate",
    responses={
        200: {"description": "City validation result"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    summary="Validate city support",
    description="Check if a city is supported by the weather API",
)
async def validate_city(
    city: str = Path(
        ...,
        description="Name of the city to validate",
        min_length=1,
        max_length=100,
        example="paris"
    )
) -> dict[str, bool | str]:
    """
    Validate if a city is supported by the weather API.

    This endpoint checks whether the specified city is available
    for weather data retrieval without making a full weather request.

    Args:
        city: Name of the city to validate (case-insensitive).

    Returns:
        Dictionary containing validation result and city name.

    Raises:
        HTTPException: 500 if an internal error occurs.
    """
    try:
        is_supported = await weather_service.validate_city(city)

        return {
            "city": city,
            "is_supported": is_supported,
            "message": f"City '{city}' is {'supported' if is_supported else 'not supported'}"
        }

    except Exception as e:
        logger.error(
            "Failed to validate city",
            city=city,
            error=str(e),
            exc_info=True
        )
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Internal server error",
                "error_code": "INTERNAL_ERROR",
                "details": {"message": "An unexpected error occurred"}
            }
        )
