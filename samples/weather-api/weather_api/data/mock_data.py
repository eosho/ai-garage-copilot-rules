"""
Mock data provider for the weather API service.

This module provides realistic mock weather data for testing and demonstration
purposes. It includes current weather and forecast data for various cities.
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from models.schemas import (
    CurrentWeather,
    ForecastDay,
    SupportedCity,
    Temperature,
    WeatherCondition,
    WeatherConditionDetails,
    WeatherForecast,
    Wind,
    WindDirection,
)


class MockWeatherData:
    """Provider for mock weather data."""

    # Supported cities with their coordinates and details
    CITIES: Dict[str, SupportedCity] = {
        "new-york": SupportedCity(
            name="New York",
            country="United States",
            region="New York",
            coordinates={"latitude": 40.7128, "longitude": -74.0060},
            timezone="America/New_York",
            population=8336817,
        ),
        "london": SupportedCity(
            name="London",
            country="United Kingdom",
            region="England",
            coordinates={"latitude": 51.5074, "longitude": -0.1278},
            timezone="Europe/London",
            population=9648110,
        ),
        "tokyo": SupportedCity(
            name="Tokyo",
            country="Japan",
            region="Kanto",
            coordinates={"latitude": 35.6762, "longitude": 139.6503},
            timezone="Asia/Tokyo",
            population=13960000,
        ),
        "paris": SupportedCity(
            name="Paris",
            country="France",
            region="Île-de-France",
            coordinates={"latitude": 48.8566, "longitude": 2.3522},
            timezone="Europe/Paris",
            population=2148327,
        ),
        "sydney": SupportedCity(
            name="Sydney",
            country="Australia",
            region="New South Wales",
            coordinates={"latitude": -33.8688, "longitude": 151.2093},
            timezone="Australia/Sydney",
            population=5312163,
        ),
        "toronto": SupportedCity(
            name="Toronto",
            country="Canada",
            region="Ontario",
            coordinates={"latitude": 43.6532, "longitude": -79.3832},
            timezone="America/Toronto",
            population=2794356,
        ),
        "mumbai": SupportedCity(
            name="Mumbai",
            country="India",
            region="Maharashtra",
            coordinates={"latitude": 19.0760, "longitude": 72.8777},
            timezone="Asia/Kolkata",
            population=20411274,
        ),
        "berlin": SupportedCity(
            name="Berlin",
            country="Germany",
            region="Berlin",
            coordinates={"latitude": 52.5200, "longitude": 13.4050},
            timezone="Europe/Berlin",
            population=3769495,
        ),
        "sao-paulo": SupportedCity(
            name="São Paulo",
            country="Brazil",
            region="São Paulo",
            coordinates={"latitude": -23.5505, "longitude": -46.6333},
            timezone="America/Sao_Paulo",
            population=12396372,
        ),
        "cape-town": SupportedCity(
            name="Cape Town",
            country="South Africa",
            region="Western Cape",
            coordinates={"latitude": -33.9249, "longitude": 18.4241},
            timezone="Africa/Johannesburg",
            population=4618000,
        ),
    }

    # Weather condition templates with realistic data
    WEATHER_CONDITIONS = {
        WeatherCondition.SUNNY: WeatherConditionDetails(
            condition=WeatherCondition.SUNNY,
            description="Clear sunny skies",
            icon="sun",
            visibility_km=15.0,
            uv_index=8,
        ),
        WeatherCondition.CLOUDY: WeatherConditionDetails(
            condition=WeatherCondition.CLOUDY,
            description="Overcast and cloudy",
            icon="cloud",
            visibility_km=10.0,
            uv_index=3,
        ),
        WeatherCondition.PARTLY_CLOUDY: WeatherConditionDetails(
            condition=WeatherCondition.PARTLY_CLOUDY,
            description="Partly cloudy with some sun",
            icon="partly-cloudy",
            visibility_km=12.0,
            uv_index=5,
        ),
        WeatherCondition.RAINY: WeatherConditionDetails(
            condition=WeatherCondition.RAINY,
            description="Light to moderate rain",
            icon="rain",
            visibility_km=5.0,
            uv_index=1,
        ),
        WeatherCondition.STORMY: WeatherConditionDetails(
            condition=WeatherCondition.STORMY,
            description="Thunderstorms with heavy rain",
            icon="storm",
            visibility_km=2.0,
            uv_index=0,
        ),
        WeatherCondition.SNOWY: WeatherConditionDetails(
            condition=WeatherCondition.SNOWY,
            description="Snow showers",
            icon="snow",
            visibility_km=3.0,
            uv_index=1,
        ),
        WeatherCondition.FOGGY: WeatherConditionDetails(
            condition=WeatherCondition.FOGGY,
            description="Dense fog",
            icon="fog",
            visibility_km=0.5,
            uv_index=1,
        ),
        WeatherCondition.WINDY: WeatherConditionDetails(
            condition=WeatherCondition.WINDY,
            description="Strong winds",
            icon="wind",
            visibility_km=12.0,
            uv_index=4,
        ),
    }

    @classmethod
    def get_supported_cities(cls) -> List[SupportedCity]:
        """
        Get list of all supported cities.

        Returns:
            List of SupportedCity objects containing city information.
        """
        return list(cls.CITIES.values())

    @classmethod
    def get_city_by_name(cls, city_name: str) -> Optional[SupportedCity]:
        """
        Get city information by name (case-insensitive).

        Args:
            city_name: Name of the city to look up.

        Returns:
            SupportedCity object if found, None otherwise.
        """
        # Normalize city name for lookup
        normalized_name = city_name.lower().replace(" ", "-").replace("_", "-")
        return cls.CITIES.get(normalized_name)

    @classmethod
    def _generate_temperature(cls, base_temp: float, variation: float = 5.0) -> Temperature:
        """
        Generate temperature with random variation.

        Args:
            base_temp: Base temperature in Celsius.
            variation: Maximum variation from base temperature.

        Returns:
            Temperature object with all units calculated.
        """
        actual_temp = base_temp + random.uniform(-variation, variation)
        return Temperature(celsius=round(actual_temp, 1))

    @classmethod
    def _generate_wind(cls) -> Wind:
        """
        Generate realistic wind data.

        Returns:
            Wind object with speed and direction.
        """
        speed_kph = random.uniform(5, 25)
        gust_kph = speed_kph + random.uniform(5, 15) if random.random() > 0.5 else None

        return Wind(
            speed_kph=round(speed_kph, 1),
            direction=random.choice(list(WindDirection)),
            gust_kph=round(gust_kph, 1) if gust_kph else None,
        )

    @classmethod
    def _get_seasonal_base_temp(cls, city: SupportedCity) -> float:
        """
        Get seasonal base temperature for a city.

        Args:
            city: City to get temperature for.

        Returns:
            Base temperature in Celsius considering location and season.
        """
        # Simple temperature mapping based on latitude and current month
        latitude = city.coordinates["latitude"]
        month = datetime.now().month

        # Temperature adjustments based on hemisphere and season
        if latitude > 0:  # Northern hemisphere
            if month in [12, 1, 2]:  # Winter
                base_temp = 0 - abs(latitude) * 0.5
            elif month in [6, 7, 8]:  # Summer
                base_temp = 25 - abs(latitude) * 0.3
            else:  # Spring/Fall
                base_temp = 15 - abs(latitude) * 0.4
        else:  # Southern hemisphere
            if month in [6, 7, 8]:  # Winter
                base_temp = 5 + abs(latitude) * 0.3
            elif month in [12, 1, 2]:  # Summer
                base_temp = 25 + abs(latitude) * 0.2
            else:  # Spring/Fall
                base_temp = 15 + abs(latitude) * 0.1

        # Coastal vs inland adjustments
        if abs(city.coordinates["longitude"]) < 10:  # Rough coastal indicator
            base_temp += 3  # Coastal areas are generally milder

        return max(-30, min(50, base_temp))  # Realistic temperature bounds

    @classmethod
    def generate_current_weather(cls, city_name: str) -> Optional[CurrentWeather]:
        """
        Generate current weather data for a city.

        Args:
            city_name: Name of the city to generate weather for.

        Returns:
            CurrentWeather object if city is supported, None otherwise.
        """
        city = cls.get_city_by_name(city_name)
        if not city:
            return None

        # Generate realistic weather based on location
        base_temp = cls._get_seasonal_base_temp(city)
        current_temp = cls._generate_temperature(base_temp)
        feels_like_temp = cls._generate_temperature(base_temp, 3.0)

        # Select random weather condition
        condition = random.choice(list(cls.WEATHER_CONDITIONS.values()))

        # Generate other weather parameters
        humidity = random.randint(30, 90)
        pressure_mb = random.uniform(990, 1030)
        wind = cls._generate_wind()

        now = datetime.now()

        return CurrentWeather(
            city=city.name,
            country=city.country,
            region=city.region,
            coordinates=city.coordinates,
            temperature=current_temp,
            feels_like=feels_like_temp,
            humidity=humidity,
            pressure_mb=round(pressure_mb, 1),
            wind=wind,
            condition=condition,
            last_updated=now,
            local_time=now,  # Simplified - would need timezone conversion in real app
        )

    @classmethod
    def generate_weather_forecast(cls, city_name: str, days: int = 5) -> Optional[WeatherForecast]:
        """
        Generate weather forecast for a city.

        Args:
            city_name: Name of the city to generate forecast for.
            days: Number of days to forecast (max 10).

        Returns:
            WeatherForecast object if city is supported, None otherwise.
        """
        city = cls.get_city_by_name(city_name)
        if not city:
            return None

        days = min(days, 10)  # Limit to maximum 10 days
        base_temp = cls._get_seasonal_base_temp(city)

        forecast_days = []

        for i in range(days):
            date = datetime.now() + timedelta(days=i)

            # Generate daily temperatures with some variation
            daily_variation = random.uniform(-2, 2)
            temp_max = cls._generate_temperature(base_temp + 5 + daily_variation, 3.0)
            temp_min = cls._generate_temperature(base_temp - 5 + daily_variation, 3.0)
            temp_avg = cls._generate_temperature(base_temp + daily_variation, 2.0)

            # Ensure logical temperature relationships
            if temp_min.celsius > temp_max.celsius:
                temp_min, temp_max = temp_max, temp_min

            condition = random.choice(list(cls.WEATHER_CONDITIONS.values()))
            wind = cls._generate_wind()

            # Generate precipitation based on weather condition
            if condition.condition in [WeatherCondition.RAINY, WeatherCondition.STORMY]:
                precipitation_mm = random.uniform(1, 15)
                precipitation_chance = random.randint(60, 95)
            elif condition.condition == WeatherCondition.SNOWY:
                precipitation_mm = random.uniform(0.5, 8)
                precipitation_chance = random.randint(50, 85)
            else:
                precipitation_mm = random.uniform(0, 0.5)
                precipitation_chance = random.randint(0, 20)

            forecast_day = ForecastDay(
                date=date.strftime("%Y-%m-%d"),
                temperature_max=temp_max,
                temperature_min=temp_min,
                temperature_avg=temp_avg,
                condition=condition,
                humidity_avg=random.randint(40, 80),
                wind_max=wind,
                precipitation_mm=round(precipitation_mm, 1),
                precipitation_chance=precipitation_chance,
                sunrise="06:30",  # Simplified - would need solar calculations
                sunset="18:45",   # Simplified - would need solar calculations
            )

            forecast_days.append(forecast_day)

        return WeatherForecast(
            city=city.name,
            country=city.country,
            region=city.region,
            coordinates=city.coordinates,
            forecast_days=forecast_days,
            generated_at=datetime.now(),
        )
