"""
Tests for weather API endpoints.

This module contains comprehensive tests for all weather API endpoints,
including success cases, error handling, and edge cases.
"""

import pytest
from fastapi.testclient import TestClient

from weather_api.main import app

client = TestClient(app)


class TestCurrentWeatherEndpoint:
    """Test cases for the current weather endpoint."""
    
    def test_get_current_weather_success(self):
        """Test successful current weather retrieval."""
        response = client.get("/weather/current/london")
        
        assert response.status_code == 200
        data = response.json()
        
        # Validate response structure
        assert "city" in data
        assert "country" in data
        assert "temperature" in data
        assert "humidity" in data
        assert "condition" in data
        assert "last_updated" in data
        
        # Validate specific fields
        assert data["city"] == "London"
        assert data["country"] == "United Kingdom"
        assert isinstance(data["temperature"]["celsius"], float)
        assert isinstance(data["humidity"], int)
        assert 0 <= data["humidity"] <= 100
    
    def test_get_current_weather_case_insensitive(self):
        """Test that city names are case-insensitive."""
        responses = [
            client.get("/weather/current/LONDON"),
            client.get("/weather/current/london"),
            client.get("/weather/current/London"),
        ]
        
        for response in responses:
            assert response.status_code == 200
            data = response.json()
            assert data["city"] == "London"
    
    def test_get_current_weather_city_not_found(self):
        """Test error handling for unsupported cities."""
        response = client.get("/weather/current/atlantis")
        
        assert response.status_code == 404
        data = response.json()
        
        assert "error" in data["detail"]
        assert "error_code" in data["detail"]
        assert data["detail"]["error_code"] == "CITY_NOT_FOUND"
    
    def test_get_current_weather_empty_city(self):
        """Test error handling for empty city name."""
        response = client.get("/weather/current/ ")
        
        assert response.status_code == 422
    
    def test_get_current_weather_response_headers(self):
        """Test that response includes correlation headers."""
        response = client.get("/weather/current/tokyo")
        
        assert response.status_code == 200
        assert "X-Correlation-ID" in response.headers
        assert "X-Process-Time" in response.headers


class TestWeatherForecastEndpoint:
    """Test cases for the weather forecast endpoint."""
    
    def test_get_weather_forecast_success(self):
        """Test successful weather forecast retrieval."""
        response = client.get("/weather/forecast/tokyo")
        
        assert response.status_code == 200
        data = response.json()
        
        # Validate response structure
        assert "city" in data
        assert "country" in data
        assert "forecast_days" in data
        assert "generated_at" in data
        
        # Validate forecast data
        assert data["city"] == "Tokyo"
        assert len(data["forecast_days"]) == 5  # Default days
        
        for day in data["forecast_days"]:
            assert "date" in day
            assert "temperature_max" in day
            assert "temperature_min" in day
            assert "condition" in day
            assert "precipitation_chance" in day
    
    def test_get_weather_forecast_custom_days(self):
        """Test forecast with custom number of days."""
        response = client.get("/weather/forecast/paris?days=3")
        
        assert response.status_code == 200
        data = response.json()
        
        assert len(data["forecast_days"]) == 3
    
    def test_get_weather_forecast_max_days(self):
        """Test forecast with maximum allowed days."""
        response = client.get("/weather/forecast/berlin?days=10")
        
        assert response.status_code == 200
        data = response.json()
        
        assert len(data["forecast_days"]) == 10
    
    def test_get_weather_forecast_invalid_days(self):
        """Test error handling for invalid days parameter."""
        # Test days > 10
        response = client.get("/weather/forecast/sydney?days=15")
        assert response.status_code == 422
        
        # Test days < 1
        response = client.get("/weather/forecast/sydney?days=0")
        assert response.status_code == 422
    
    def test_get_weather_forecast_city_not_found(self):
        """Test error handling for unsupported cities."""
        response = client.get("/weather/forecast/atlantis")
        
        assert response.status_code == 404
        data = response.json()
        
        assert data["detail"]["error_code"] == "CITY_NOT_FOUND"


class TestSupportedCitiesEndpoint:
    """Test cases for the supported cities endpoint."""
    
    def test_get_supported_cities_success(self):
        """Test successful retrieval of supported cities."""
        response = client.get("/weather/cities")
        
        assert response.status_code == 200
        data = response.json()
        
        # Validate response structure
        assert "cities" in data
        assert "total_count" in data
        assert isinstance(data["cities"], list)
        assert data["total_count"] > 0
        
        # Validate city data
        for city in data["cities"]:
            assert "name" in city
            assert "country" in city
            assert "coordinates" in city
            assert "timezone" in city
            assert "latitude" in city["coordinates"]
            assert "longitude" in city["coordinates"]
    
    def test_get_supported_cities_search(self):
        """Test city search functionality."""
        response = client.get("/weather/cities?search=new")
        
        assert response.status_code == 200
        data = response.json()
        
        # Should find "New York"
        assert data["total_count"] > 0
        city_names = [city["name"] for city in data["cities"]]
        assert any("New" in name for name in city_names)
    
    def test_get_supported_cities_search_no_results(self):
        """Test city search with no results."""
        response = client.get("/weather/cities?search=atlantis")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["total_count"] == 0
        assert len(data["cities"]) == 0


class TestCityValidationEndpoint:
    """Test cases for the city validation endpoint."""
    
    def test_validate_city_supported(self):
        """Test validation of a supported city."""
        response = client.get("/weather/cities/london/validate")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["city"] == "london"
        assert data["is_supported"] is True
        assert "supported" in data["message"]
    
    def test_validate_city_not_supported(self):
        """Test validation of an unsupported city."""
        response = client.get("/weather/cities/atlantis/validate")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["city"] == "atlantis"
        assert data["is_supported"] is False
        assert "not supported" in data["message"]


class TestHealthAndSystemEndpoints:
    """Test cases for health and system endpoints."""
    
    def test_health_check(self):
        """Test health check endpoint."""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["status"] == "healthy"
        assert data["service"] == "weather-api"
        assert data["version"] == "0.1.0"
    
    def test_root_endpoint(self):
        """Test root endpoint."""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["service"] == "Weather API"
        assert data["version"] == "0.1.0"
        assert "docs" in data
        assert "health" in data


class TestAPIDocumentation:
    """Test cases for API documentation endpoints."""
    
    def test_openapi_schema(self):
        """Test OpenAPI schema endpoint."""
        response = client.get("/openapi.json")
        
        assert response.status_code == 200
        schema = response.json()
        
        assert "openapi" in schema
        assert "info" in schema
        assert "paths" in schema
        assert schema["info"]["title"] == "Weather API"
    
    def test_docs_endpoint(self):
        """Test interactive documentation endpoint."""
        response = client.get("/docs")
        
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
    
    def test_redoc_endpoint(self):
        """Test alternative documentation endpoint."""
        response = client.get("/redoc")
        
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]


class TestErrorHandling:
    """Test cases for error handling and edge cases."""
    
    def test_invalid_endpoint(self):
        """Test handling of invalid endpoints."""
        response = client.get("/weather/invalid-endpoint")
        
        assert response.status_code == 404
    
    def test_method_not_allowed(self):
        """Test handling of incorrect HTTP methods."""
        response = client.post("/weather/current/london")
        
        assert response.status_code == 405
    
    def test_cors_headers(self):
        """Test CORS headers are present."""
        response = client.get("/weather/current/london")
        
        assert response.status_code == 200
        # CORS headers should be added by middleware


@pytest.mark.asyncio
class TestAsyncBehavior:
    """Test cases for async behavior and concurrency."""
    
    async def test_concurrent_requests(self):
        """Test handling of concurrent requests."""
        import asyncio
        import httpx
        
        async with httpx.AsyncClient(app=app, base_url="http://test") as client:
            tasks = [
                client.get("/weather/current/london"),
                client.get("/weather/current/tokyo"),
                client.get("/weather/current/paris"),
            ]
            
            responses = await asyncio.gather(*tasks)
            
            for response in responses:
                assert response.status_code == 200
