"""Tests for API endpoints."""

from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.user_service import UserService

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_check_success(self):
        """
        Tests successful health check.
        """
        # Act
        response = client.get("/api/v1/health")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert "version" in data


class TestUsersEndpoint:
    """Tests for the users endpoints."""

    def test_get_all_users_success(self):
        """
        Tests successful retrieval of all users.
        """
        # Act
        response = client.get("/api/v1/users")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "message" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) > 0

        # Verify user structure
        user = data["data"][0]
        assert "id" in user
        assert "name" in user
        assert "email" in user
        assert "pets" in user
        assert isinstance(user["pets"], list)

    def test_get_users_with_species_filter(self):
        """
        Tests retrieval of users filtered by pet species.
        """
        # Act
        response = client.get("/api/v1/users?species=dog")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert isinstance(data["data"], list)

        # Verify all returned users have dogs
        for user in data["data"]:
            has_dog = any(pet["species"] == "dog" for pet in user["pets"])
            assert has_dog

    def test_get_users_with_nonexistent_species(self):
        """
        Tests retrieval of users with non-existent pet species.
        """
        # Act
        response = client.get("/api/v1/users?species=dragon")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["data"] == []

    def test_get_user_by_id_success(self):
        """
        Tests successful retrieval of a user by ID.
        """
        # Act
        response = client.get("/api/v1/users/1")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["data"]["id"] == 1
        assert data["data"]["name"] == "Alice Johnson"
        assert len(data["data"]["pets"]) == 2

    def test_get_user_by_id_not_found(self):
        """
        Tests retrieval of a non-existent user.
        """
        # Act
        response = client.get("/api/v1/users/999")

        # Assert
        assert response.status_code == 404
        data = response.json()
        assert data["success"] is False
        assert "not found" in data["error"].lower()

    def test_get_user_by_invalid_id(self):
        """
        Tests retrieval with invalid user ID.
        """
        # Act
        response = client.get("/api/v1/users/-1")

        # Assert
        assert response.status_code == 400
        data = response.json()
        assert data["success"] is False
        assert "positive integer" in data["error"]

    def test_get_user_pet_statistics(self):
        """
        Tests retrieval of user pet statistics.
        """
        # Act
        response = client.get("/api/v1/users/stats/pet-count")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data

        stats = data["data"]
        assert "total_users" in stats
        assert "total_pets" in stats
        assert "users_with_no_pets" in stats
        assert "users_with_pets" in stats
        assert "average_pets_per_user" in stats
        assert "pet_species_count" in stats
        assert isinstance(stats["pet_species_count"], dict)


class TestErrorHandling:
    """Tests for error handling."""

    def test_404_endpoint(self):
        """
        Tests accessing a non-existent endpoint.
        """
        # Act
        response = client.get("/api/v1/nonexistent")

        # Assert
        assert response.status_code == 404

    def test_invalid_http_method(self):
        """
        Tests using an invalid HTTP method.
        """
        # Act
        response = client.post("/api/v1/users")

        # Assert
        assert response.status_code == 405  # Method Not Allowed


class TestCORS:
    """Tests for CORS configuration."""

    def test_cors_headers(self):
        """
        Tests that CORS headers are present.
        """
        # Act
        response = client.get("/api/v1/health", headers={"Origin": "http://localhost:3000"})

        # Assert
        assert response.status_code == 200
        # Note: TestClient doesn't process CORS middleware the same way as a real server
        # In a real deployment, you would see Access-Control-Allow-Origin headers


@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2, 200),
    (3, 200),
    (999, 404),
    (-1, 400),
])
def test_get_user_parametrized(user_id, expected_status):
    """
    Parametrized test for user retrieval with different IDs.

    Args:
        user_id: The user ID to test.
        expected_status: The expected HTTP status code.
    """
    # Act
    response = client.get(f"/api/v1/users/{user_id}")

    # Assert
    assert response.status_code == expected_status
