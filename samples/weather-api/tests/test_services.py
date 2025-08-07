"""
Tests for weather service business logic.

This module contains tests for the WeatherService class,
including mock data generation and service methods.
"""

import pytest

from weather_api.data.mock_data import MockWeatherData
from weather_api.models.schemas import WeatherCondition
from weather_api.services.weather_service import WeatherService


class TestMockWeatherData:
    """Test cases for the MockWeatherData class."""
    
    def test_get_supported_cities(self):
        """Test retrieval of supported cities."""
        cities = MockWeatherData.get_supported_cities()
        
        assert len(cities) > 0
        
        # Check that all required fields are present
        for city in cities:
            assert city.name
            assert city.country
            assert city.coordinates
            assert "latitude" in city.coordinates
            assert "longitude" in city.coordinates
            assert city.timezone
    
    def test_get_city_by_name_success(self):
        """Test successful city lookup by name."""
        city = MockWeatherData.get_city_by_name("london")
        
        assert city is not None
        assert city.name == "London"
        assert city.country == "United Kingdom"
    
    def test_get_city_by_name_case_insensitive(self):
        """Test that city lookup is case-insensitive."""
        test_cases = ["LONDON", "london", "London", "LoNdOn"]
        
        for case in test_cases:
            city = MockWeatherData.get_city_by_name(case)
            assert city is not None
            assert city.name == "London"
    
    def test_get_city_by_name_with_spaces(self):
        """Test city lookup with spaces and hyphens."""
        city = MockWeatherData.get_city_by_name("new york")
        
        assert city is not None
        assert city.name == "New York"
    
    def test_get_city_by_name_not_found(self):
        """Test city lookup for non-existent city."""
        city = MockWeatherData.get_city_by_name("atlantis")
        
        assert city is None
    
    def test_generate_current_weather_success(self):
        """Test successful current weather generation."""
        weather = MockWeatherData.generate_current_weather("tokyo")
        
        assert weather is not None
        assert weather.city == "Tokyo"
        assert weather.country == "Japan"
        
        # Validate temperature data
        assert isinstance(weather.temperature.celsius, float)
        assert isinstance(weather.temperature.fahrenheit, float)
        assert isinstance(weather.temperature.kelvin, float)
        
        # Check temperature conversions are correct
        celsius = weather.temperature.celsius
        fahrenheit = weather.temperature.fahrenheit
        kelvin = weather.temperature.kelvin
        
        expected_fahrenheit = (celsius * 9/5) + 32
        expected_kelvin = celsius + 273.15
        
        assert abs(fahrenheit - expected_fahrenheit) < 0.01
        assert abs(kelvin - expected_kelvin) < 0.01
        
        # Validate other fields
        assert 0 <= weather.humidity <= 100
        assert weather.pressure_mb > 0
        assert weather.pressure_in > 0
        assert weather.wind.speed_kph >= 0
        assert weather.wind.speed_mph >= 0
        assert weather.condition.condition in WeatherCondition
    
    def test_generate_current_weather_not_found(self):
        """Test current weather generation for non-existent city."""
        weather = MockWeatherData.generate_current_weather("atlantis")
        
        assert weather is None
    
    def test_generate_weather_forecast_success(self):
        """Test successful weather forecast generation."""
        forecast = MockWeatherData.generate_weather_forecast("paris", 3)
        
        assert forecast is not None
        assert forecast.city == "Paris"
        assert forecast.country == "France"
        assert len(forecast.forecast_days) == 3
        
        # Validate forecast days
        for day in forecast.forecast_days:
            assert day.date
            assert isinstance(day.temperature_max.celsius, float)
            assert isinstance(day.temperature_min.celsius, float)
            assert isinstance(day.temperature_avg.celsius, float)
            
            # Temperature logic validation
            assert day.temperature_min.celsius <= day.temperature_avg.celsius <= day.temperature_max.celsius
            
            assert 0 <= day.humidity_avg <= 100
            assert 0 <= day.precipitation_chance <= 100
            assert day.precipitation_mm >= 0
            assert day.condition.condition in WeatherCondition
    
    def test_generate_weather_forecast_max_days(self):
        """Test forecast generation with maximum days limit."""
        forecast = MockWeatherData.generate_weather_forecast("berlin", 15)
        
        assert forecast is not None
        assert len(forecast.forecast_days) == 10  # Should be limited to 10
    
    def test_generate_weather_forecast_not_found(self):
        """Test forecast generation for non-existent city."""
        forecast = MockWeatherData.generate_weather_forecast("atlantis")
        
        assert forecast is None


class TestWeatherService:
    """Test cases for the WeatherService class."""
    
    @pytest.fixture
    def weather_service(self):
        """Create a WeatherService instance for testing."""
        return WeatherService()
    
    @pytest.mark.asyncio
    async def test_get_current_weather_success(self, weather_service):
        """Test successful current weather retrieval."""
        weather = await weather_service.get_current_weather("london")
        
        assert weather is not None
        assert weather.city == "London"
        assert weather.country == "United Kingdom"
    
    @pytest.mark.asyncio
    async def test_get_current_weather_not_found(self, weather_service):
        """Test current weather retrieval for non-existent city."""
        weather = await weather_service.get_current_weather("atlantis")
        
        assert weather is None
    
    @pytest.mark.asyncio
    async def test_get_current_weather_empty_city(self, weather_service):
        """Test error handling for empty city name."""
        with pytest.raises(ValueError, match="City name cannot be empty"):
            await weather_service.get_current_weather("")
    
    @pytest.mark.asyncio
    async def test_get_current_weather_whitespace_city(self, weather_service):
        """Test error handling for whitespace-only city name."""
        with pytest.raises(ValueError, match="City name cannot be empty"):
            await weather_service.get_current_weather("   ")
    
    @pytest.mark.asyncio
    async def test_get_weather_forecast_success(self, weather_service):
        """Test successful weather forecast retrieval."""
        forecast = await weather_service.get_weather_forecast("tokyo", 5)
        
        assert forecast is not None
        assert forecast.city == "Tokyo"
        assert len(forecast.forecast_days) == 5
    
    @pytest.mark.asyncio
    async def test_get_weather_forecast_invalid_days(self, weather_service):
        """Test error handling for invalid days parameter."""
        with pytest.raises(ValueError, match="Forecast days must be between 1 and 10"):
            await weather_service.get_weather_forecast("tokyo", 0)
        
        with pytest.raises(ValueError, match="Forecast days must be between 1 and 10"):
            await weather_service.get_weather_forecast("tokyo", 15)
    
    @pytest.mark.asyncio
    async def test_get_supported_cities(self, weather_service):
        """Test retrieval of supported cities."""
        response = await weather_service.get_supported_cities()
        
        assert response.total_count > 0
        assert len(response.cities) == response.total_count
        assert len(response.cities) > 5  # Should have multiple cities
    
    @pytest.mark.asyncio
    async def test_validate_city_supported(self, weather_service):
        """Test validation of supported city."""
        is_supported = await weather_service.validate_city("paris")
        
        assert is_supported is True
    
    @pytest.mark.asyncio
    async def test_validate_city_not_supported(self, weather_service):
        """Test validation of unsupported city."""
        is_supported = await weather_service.validate_city("atlantis")
        
        assert is_supported is False
    
    @pytest.mark.asyncio
    async def test_validate_city_empty(self, weather_service):
        """Test validation of empty city name."""
        is_supported = await weather_service.validate_city("")
        
        assert is_supported is False
    
    @pytest.mark.asyncio
    async def test_search_cities_success(self, weather_service):
        """Test successful city search."""
        cities = await weather_service.search_cities("new")
        
        assert len(cities) > 0
        
        # Should find "New York"
        city_names = [city.name for city in cities]
        assert any("New" in name for name in city_names)
    
    @pytest.mark.asyncio
    async def test_search_cities_no_results(self, weather_service):
        """Test city search with no results."""
        cities = await weather_service.search_cities("atlantis")
        
        assert len(cities) == 0
    
    @pytest.mark.asyncio
    async def test_search_cities_empty_query(self, weather_service):
        """Test city search with empty query."""
        cities = await weather_service.search_cities("")
        
        assert len(cities) == 0
    
    @pytest.mark.asyncio
    async def test_search_cities_by_country(self, weather_service):
        """Test city search by country name."""
        cities = await weather_service.search_cities("japan")
        
        assert len(cities) > 0
        
        # Should find cities in Japan
        for city in cities:
            assert "Japan" in city.country
    
    @pytest.mark.asyncio
    async def test_search_cities_case_insensitive(self, weather_service):
        """Test that city search is case-insensitive."""
        results_lower = await weather_service.search_cities("london")
        results_upper = await weather_service.search_cities("LONDON")
        results_mixed = await weather_service.search_cities("London")
        
        assert len(results_lower) == len(results_upper) == len(results_mixed)
        assert len(results_lower) > 0


class TestTemperatureConversions:
    """Test cases for temperature conversion logic."""
    
    def test_temperature_conversion_from_celsius(self):
        """Test temperature conversions from Celsius."""
        from weather_api.models.schemas import Temperature
        
        temp = Temperature(celsius=0.0)
        
        assert temp.celsius == 0.0
        assert temp.fahrenheit == 32.0
        assert temp.kelvin == 273.15
    
    def test_temperature_conversion_negative_celsius(self):
        """Test temperature conversions with negative Celsius."""
        from weather_api.models.schemas import Temperature
        
        temp = Temperature(celsius=-10.0)
        
        assert temp.celsius == -10.0
        assert temp.fahrenheit == 14.0
        assert temp.kelvin == 263.15
    
    def test_temperature_conversion_explicit_values(self):
        """Test temperature with explicitly provided values."""
        from weather_api.models.schemas import Temperature
        
        temp = Temperature(
            celsius=20.0,
            fahrenheit=70.0,  # Not the calculated value
            kelvin=300.0      # Not the calculated value
        )
        
        # Should use provided values, not calculated ones
        assert temp.celsius == 20.0
        assert temp.fahrenheit == 70.0
        assert temp.kelvin == 300.0


class TestWindConversions:
    """Test cases for wind speed conversion logic."""
    
    def test_wind_speed_conversion(self):
        """Test wind speed conversion from kph to mph."""
        from weather_api.models.schemas import Wind, WindDirection
        
        wind = Wind(
            speed_kph=100.0,
            direction=WindDirection.NORTH
        )
        
        assert wind.speed_kph == 100.0
        assert abs(wind.speed_mph - 62.1371) < 0.01
    
    def test_wind_speed_explicit_mph(self):
        """Test wind with explicitly provided mph value."""
        from weather_api.models.schemas import Wind, WindDirection
        
        wind = Wind(
            speed_kph=100.0,
            speed_mph=50.0,  # Not the calculated value
            direction=WindDirection.EAST
        )
        
        # Should use provided value, not calculated one
        assert wind.speed_kph == 100.0
        assert wind.speed_mph == 50.0
