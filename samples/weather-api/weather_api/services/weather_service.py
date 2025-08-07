"""
Weather service implementation.

This module provides the business logic for weather data operations,
including current weather retrieval, forecasting, and city management.
"""

import asyncio
from typing import List, Optional

from core.config import get_settings
from core.logging_config import get_logger
from data.mock_data import MockWeatherData
from models.schemas import (
    CurrentWeather,
    SupportedCitiesResponse,
    SupportedCity,
    WeatherForecast,
)


class WeatherService:
    """
    Service class for weather-related operations.

    This class provides methods for retrieving current weather data,
    weather forecasts, and managing supported cities.
    """

    def __init__(self) -> None:
        """Initialize the weather service."""
        self.settings = get_settings()
        self.logger = get_logger(__name__)
        self.mock_data = MockWeatherData()

    async def _simulate_api_delay(self) -> None:
        """
        Simulate API response delay for testing purposes.

        Adds configurable delay to simulate real API latency
        when mock_response_delay_ms is set in configuration.
        """
        if self.settings.mock_response_delay_ms > 0:
            delay_seconds = self.settings.mock_response_delay_ms / 1000
            await asyncio.sleep(delay_seconds)

    async def get_current_weather(self, city_name: str) -> Optional[CurrentWeather]:
        """
        Get current weather data for a specified city.

        Args:
            city_name: Name of the city to get weather for.

        Returns:
            CurrentWeather object if city is supported, None otherwise.

        Raises:
            ValueError: If city_name is empty or invalid.
        """
        if not city_name or not city_name.strip():
            raise ValueError("City name cannot be empty")

        city_name = city_name.strip()

        self.logger.info(
            "Fetching current weather",
            city=city_name,
            service="weather"
        )

        # Simulate API delay
        await self._simulate_api_delay()

        try:
            weather_data = self.mock_data.generate_current_weather(city_name)

            if weather_data:
                self.logger.info(
                    "Current weather retrieved successfully",
                    city=weather_data.city,
                    country=weather_data.country,
                    temperature=weather_data.temperature.celsius,
                    condition=weather_data.condition.condition
                )
            else:
                self.logger.warning(
                    "City not found",
                    city=city_name,
                    supported_cities=list(self.mock_data.CITIES.keys())
                )

            return weather_data

        except Exception as e:
            self.logger.error(
                "Failed to retrieve current weather",
                city=city_name,
                error=str(e),
                exc_info=True
            )
            raise

    async def get_weather_forecast(
        self,
        city_name: str,
        days: int = 5
    ) -> Optional[WeatherForecast]:
        """
        Get weather forecast for a specified city.

        Args:
            city_name: Name of the city to get forecast for.
            days: Number of days to forecast (1-10, default 5).

        Returns:
            WeatherForecast object if city is supported, None otherwise.

        Raises:
            ValueError: If city_name is empty or days is out of range.
        """
        if not city_name or not city_name.strip():
            raise ValueError("City name cannot be empty")

        if not 1 <= days <= 10:
            raise ValueError("Forecast days must be between 1 and 10")

        city_name = city_name.strip()

        self.logger.info(
            "Fetching weather forecast",
            city=city_name,
            days=days,
            service="weather"
        )

        # Simulate API delay
        await self._simulate_api_delay()

        try:
            forecast_data = self.mock_data.generate_weather_forecast(city_name, days)

            if forecast_data:
                self.logger.info(
                    "Weather forecast retrieved successfully",
                    city=forecast_data.city,
                    country=forecast_data.country,
                    forecast_days=len(forecast_data.forecast_days)
                )
            else:
                self.logger.warning(
                    "City not found for forecast",
                    city=city_name,
                    supported_cities=list(self.mock_data.CITIES.keys())
                )

            return forecast_data

        except Exception as e:
            self.logger.error(
                "Failed to retrieve weather forecast",
                city=city_name,
                days=days,
                error=str(e),
                exc_info=True
            )
            raise

    async def get_supported_cities(self) -> SupportedCitiesResponse:
        """
        Get list of all supported cities.

        Returns:
            SupportedCitiesResponse containing list of cities and total count.
        """
        self.logger.info("Fetching supported cities list")

        # Simulate API delay
        await self._simulate_api_delay()

        try:
            cities = self.mock_data.get_supported_cities()

            self.logger.info(
                "Supported cities retrieved successfully",
                total_cities=len(cities)
            )

            return SupportedCitiesResponse(
                cities=cities,
                total_count=len(cities)
            )

        except Exception as e:
            self.logger.error(
                "Failed to retrieve supported cities",
                error=str(e),
                exc_info=True
            )
            raise

    async def validate_city(self, city_name: str) -> bool:
        """
        Validate if a city is supported by the service.

        Args:
            city_name: Name of the city to validate.

        Returns:
            True if city is supported, False otherwise.
        """
        if not city_name or not city_name.strip():
            return False

        city_data = self.mock_data.get_city_by_name(city_name.strip())
        return city_data is not None

    async def search_cities(self, query: str) -> List[SupportedCity]:
        """
        Search for cities matching a query string.

        Args:
            query: Search query string.

        Returns:
            List of SupportedCity objects matching the query.
        """
        if not query or not query.strip():
            return []

        query = query.strip().lower()

        self.logger.info(
            "Searching cities",
            query=query
        )

        try:
            all_cities = self.mock_data.get_supported_cities()

            # Simple search implementation
            matching_cities = [
                city for city in all_cities
                if (query in city.name.lower() or
                    query in city.country.lower() or
                    (city.region and query in city.region.lower()))
            ]

            self.logger.info(
                "City search completed",
                query=query,
                results_count=len(matching_cities)
            )

            return matching_cities

        except Exception as e:
            self.logger.error(
                "Failed to search cities",
                query=query,
                error=str(e),
                exc_info=True
            )
            raise


# Global service instance
weather_service = WeatherService()
