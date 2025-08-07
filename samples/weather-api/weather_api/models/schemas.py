"""
Pydantic models and schemas for the weather API.

This module defines all data models used for request/response serialization
and validation in the weather API service.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, validator


class WeatherCondition(str, Enum):
    """Enumeration of possible weather conditions."""
    
    SUNNY = "sunny"
    CLOUDY = "cloudy"
    PARTLY_CLOUDY = "partly_cloudy"
    RAINY = "rainy"
    STORMY = "stormy"
    SNOWY = "snowy"
    FOGGY = "foggy"
    WINDY = "windy"


class TemperatureUnit(str, Enum):
    """Enumeration of temperature units."""
    
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"
    KELVIN = "kelvin"


class WindDirection(str, Enum):
    """Enumeration of wind directions."""
    
    NORTH = "N"
    NORTHEAST = "NE"
    EAST = "E"
    SOUTHEAST = "SE"
    SOUTH = "S"
    SOUTHWEST = "SW"
    WEST = "W"
    NORTHWEST = "NW"


class Temperature(BaseModel):
    """Temperature data with multiple units."""
    
    celsius: float = Field(..., description="Temperature in Celsius", ge=-273.15)
    fahrenheit: float = Field(..., description="Temperature in Fahrenheit", ge=-459.67)
    kelvin: float = Field(..., description="Temperature in Kelvin", ge=0)
    
    @validator("fahrenheit", pre=True, always=True)
    def calculate_fahrenheit(cls, v: Optional[float], values: Dict[str, Any]) -> float:
        """
        Calculate Fahrenheit from Celsius if not provided.
        
        Args:
            v: Fahrenheit value (if provided).
            values: Other field values containing celsius.
            
        Returns:
            Fahrenheit temperature value.
        """
        if v is not None:
            return v
        celsius = values.get("celsius")
        if celsius is not None:
            return (celsius * 9/5) + 32
        return 0.0
    
    @validator("kelvin", pre=True, always=True)
    def calculate_kelvin(cls, v: Optional[float], values: Dict[str, Any]) -> float:
        """
        Calculate Kelvin from Celsius if not provided.
        
        Args:
            v: Kelvin value (if provided).
            values: Other field values containing celsius.
            
        Returns:
            Kelvin temperature value.
        """
        if v is not None:
            return v
        celsius = values.get("celsius")
        if celsius is not None:
            return celsius + 273.15
        return 273.15


class Wind(BaseModel):
    """Wind information."""
    
    speed_kph: float = Field(..., description="Wind speed in km/h", ge=0)
    speed_mph: float = Field(..., description="Wind speed in mph", ge=0)
    direction: WindDirection = Field(..., description="Wind direction")
    gust_kph: Optional[float] = Field(None, description="Wind gust speed in km/h", ge=0)
    
    @validator("speed_mph", pre=True, always=True)
    def calculate_mph(cls, v: Optional[float], values: Dict[str, Any]) -> float:
        """
        Calculate mph from kph if not provided.
        
        Args:
            v: Speed in mph (if provided).
            values: Other field values containing speed_kph.
            
        Returns:
            Wind speed in mph.
        """
        if v is not None:
            return v
        speed_kph = values.get("speed_kph")
        if speed_kph is not None:
            return speed_kph * 0.621371
        return 0.0


class WeatherConditionDetails(BaseModel):
    """Detailed weather condition information."""
    
    condition: WeatherCondition = Field(..., description="Primary weather condition")
    description: str = Field(..., description="Human-readable description")
    icon: str = Field(..., description="Weather icon identifier")
    visibility_km: float = Field(..., description="Visibility in kilometers", ge=0)
    uv_index: int = Field(..., description="UV index", ge=0, le=11)


class CurrentWeather(BaseModel):
    """Current weather data for a location."""
    
    city: str = Field(..., description="City name", min_length=1, max_length=100)
    country: str = Field(..., description="Country name", min_length=1, max_length=100)
    region: Optional[str] = Field(None, description="State or region name")
    coordinates: Dict[str, float] = Field(
        ...,
        description="Geographic coordinates",
        example={"latitude": 40.7128, "longitude": -74.0060}
    )
    
    temperature: Temperature = Field(..., description="Current temperature")
    feels_like: Temperature = Field(..., description="Feels-like temperature")
    
    humidity: int = Field(..., description="Humidity percentage", ge=0, le=100)
    pressure_mb: float = Field(..., description="Atmospheric pressure in mb", gt=0)
    pressure_in: float = Field(..., description="Atmospheric pressure in inches", gt=0)
    
    wind: Wind = Field(..., description="Wind information")
    condition: WeatherConditionDetails = Field(..., description="Weather condition")
    
    last_updated: datetime = Field(..., description="Last update timestamp")
    local_time: datetime = Field(..., description="Local time at location")
    
    @validator("pressure_in", pre=True, always=True)
    def calculate_pressure_in(cls, v: Optional[float], values: Dict[str, Any]) -> float:
        """
        Calculate pressure in inches from mb if not provided.
        
        Args:
            v: Pressure in inches (if provided).
            values: Other field values containing pressure_mb.
            
        Returns:
            Pressure in inches.
        """
        if v is not None:
            return v
        pressure_mb = values.get("pressure_mb")
        if pressure_mb is not None:
            return pressure_mb * 0.02953
        return 0.0


class ForecastDay(BaseModel):
    """Weather forecast for a single day."""
    
    date: str = Field(..., description="Date in YYYY-MM-DD format")
    temperature_max: Temperature = Field(..., description="Maximum temperature")
    temperature_min: Temperature = Field(..., description="Minimum temperature")
    temperature_avg: Temperature = Field(..., description="Average temperature")
    
    condition: WeatherConditionDetails = Field(..., description="Weather condition")
    
    humidity_avg: int = Field(..., description="Average humidity", ge=0, le=100)
    wind_max: Wind = Field(..., description="Maximum wind information")
    
    precipitation_mm: float = Field(..., description="Precipitation in mm", ge=0)
    precipitation_chance: int = Field(..., description="Chance of precipitation", ge=0, le=100)
    
    sunrise: str = Field(..., description="Sunrise time (HH:MM)")
    sunset: str = Field(..., description="Sunset time (HH:MM)")


class WeatherForecast(BaseModel):
    """Multi-day weather forecast."""
    
    city: str = Field(..., description="City name", min_length=1, max_length=100)
    country: str = Field(..., description="Country name", min_length=1, max_length=100)
    region: Optional[str] = Field(None, description="State or region name")
    coordinates: Dict[str, float] = Field(
        ...,
        description="Geographic coordinates",
        example={"latitude": 40.7128, "longitude": -74.0060}
    )
    
    forecast_days: List[ForecastDay] = Field(
        ...,
        description="Daily forecast data",
        min_items=1,
        max_items=10
    )
    
    generated_at: datetime = Field(..., description="Forecast generation timestamp")


class SupportedCity(BaseModel):
    """Information about a supported city."""
    
    name: str = Field(..., description="City name", min_length=1, max_length=100)
    country: str = Field(..., description="Country name", min_length=1, max_length=100)
    region: Optional[str] = Field(None, description="State or region name")
    coordinates: Dict[str, float] = Field(
        ...,
        description="Geographic coordinates",
        example={"latitude": 40.7128, "longitude": -74.0060}
    )
    timezone: str = Field(..., description="Timezone identifier")
    population: Optional[int] = Field(None, description="City population", ge=0)


class SupportedCitiesResponse(BaseModel):
    """Response containing list of supported cities."""
    
    cities: List[SupportedCity] = Field(..., description="List of supported cities")
    total_count: int = Field(..., description="Total number of supported cities", ge=0)


class ErrorResponse(BaseModel):
    """Error response model."""
    
    error: str = Field(..., description="Error message")
    error_code: str = Field(..., description="Error code identifier")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")
    correlation_id: Optional[str] = Field(None, description="Request correlation ID")


class HealthCheckResponse(BaseModel):
    """Health check response model."""
    
    status: str = Field(..., description="Service health status")
    service: str = Field(..., description="Service name")
    version: str = Field(..., description="Service version")
    timestamp: datetime = Field(..., description="Health check timestamp")
    uptime_seconds: float = Field(..., description="Service uptime in seconds")
