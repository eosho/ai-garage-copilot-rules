"""Tests for the user service."""

from datetime import datetime
from unittest.mock import Mock

import pytest

from app.services.user_service import UserNotFoundError, UserService


class TestUserService:
    """Tests for the UserService class."""

    @pytest.fixture
    def user_service(self):
        """Fixture for UserService instance."""
        return UserService()

    def test_get_all_users_success(self, user_service):
        """
        Tests successful retrieval of all users.
        """
        # Act
        users = user_service.get_all_users()

        # Assert
        assert len(users) == 5
        assert all(hasattr(user, 'id') for user in users)
        assert all(hasattr(user, 'name') for user in users)
        assert all(hasattr(user, 'email') for user in users)
        assert all(hasattr(user, 'pets') for user in users)

    def test_get_user_by_id_success(self, user_service):
        """
        Tests successful user retrieval by ID.
        """
        # Act
        user = user_service.get_user_by_id(1)

        # Assert
        assert user is not None
        assert user.id == 1
        assert user.name == "Alice Johnson"
        assert user.email == "alice.johnson@example.com"
        assert len(user.pets) == 2

    def test_get_user_by_id_not_found(self, user_service):
        """
        Tests user retrieval with non-existent ID.
        """
        # Act & Assert
        with pytest.raises(UserNotFoundError, match="User with ID 999 not found"):
            user_service.get_user_by_id(999)

    @pytest.mark.parametrize("invalid_id, expected_exception", [
        (-1, ValueError),
        (0, ValueError),
        ("abc", ValueError),
        (None, ValueError),
    ])
    def test_get_user_by_id_invalid_input(self, user_service, invalid_id, expected_exception):
        """
        Tests user retrieval with invalid input.

        Args:
            user_service: The UserService fixture.
            invalid_id: The invalid ID to test.
            expected_exception: The expected exception type.
        """
        # Act & Assert
        with pytest.raises(expected_exception):
            user_service.get_user_by_id(invalid_id)

    def test_get_users_by_pet_species_dog(self, user_service):
        """
        Tests filtering users by dog species.
        """
        # Act
        users = user_service.get_users_by_pet_species("dog")

        # Assert
        assert len(users) == 3  # Alice, Carol, Emma have dogs
        user_names = [user.name for user in users]
        assert "Alice Johnson" in user_names
        assert "Carol Williams" in user_names
        assert "Emma Davis" in user_names

    def test_get_users_by_pet_species_cat(self, user_service):
        """
        Tests filtering users by cat species.
        """
        # Act
        users = user_service.get_users_by_pet_species("cat")

        # Assert
        assert len(users) == 2  # Alice and Carol have cats
        user_names = [user.name for user in users]
        assert "Alice Johnson" in user_names
        assert "Carol Williams" in user_names

    def test_get_users_by_pet_species_case_insensitive(self, user_service):
        """
        Tests filtering users by species is case insensitive.
        """
        # Act
        users_lower = user_service.get_users_by_pet_species("dog")
        users_upper = user_service.get_users_by_pet_species("DOG")
        users_mixed = user_service.get_users_by_pet_species("Dog")

        # Assert
        assert len(users_lower) == len(users_upper) == len(users_mixed)
        assert users_lower[0].id == users_upper[0].id == users_mixed[0].id

    def test_get_users_by_pet_species_nonexistent(self, user_service):
        """
        Tests filtering users by non-existent species.
        """
        # Act
        users = user_service.get_users_by_pet_species("dragon")

        # Assert
        assert users == []

    def test_mock_data_structure(self, user_service):
        """
        Tests the structure of mock data.
        """
        # Act
        users = user_service.get_all_users()

        # Assert
        # Test specific user data
        alice = next(user for user in users if user.name == "Alice Johnson")
        assert alice.age == 28
        assert len(alice.pets) == 2
        assert alice.pets[0].name == "Buddy"
        assert alice.pets[0].species == "dog"
        assert alice.pets[1].name == "Whiskers"
        assert alice.pets[1].species == "cat"

        # Test user with no pets
        david = next(user for user in users if user.name == "David Brown")
        assert len(david.pets) == 0

    def test_user_created_at_timestamps(self, user_service):
        """
        Tests that users have proper created_at timestamps.
        """
        # Act
        users = user_service.get_all_users()

        # Assert
        for user in users:
            assert isinstance(user.created_at, datetime)
            assert user.created_at.year == 2023


class TestUserServiceEdgeCases:
    """Tests for edge cases in UserService."""

    @pytest.fixture
    def user_service(self):
        """Fixture for UserService instance."""
        return UserService()

    def test_empty_species_filter(self, user_service):
        """
        Tests filtering with empty string.
        """
        # Act
        users = user_service.get_users_by_pet_species("")

        # Assert
        assert users == []

    def test_whitespace_species_filter(self, user_service):
        """
        Tests filtering with whitespace.
        """
        # Act
        users = user_service.get_users_by_pet_species("   ")

        # Assert
        assert users == []
