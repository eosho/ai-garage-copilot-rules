"""User service for managing user and pet data."""

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from models.schemas import Pet, User

logger = logging.getLogger(__name__)


class UserNotFoundError(Exception):
    """Raised when a user is not found."""
    pass


class UserService:
    """Service class for managing users and their pets."""

    def __init__(self):
        """Initialize the user service with mock data."""
        self._users_data = self._get_mock_data()

    def get_all_users(self) -> List[User]:
        """
        Retrieves all users with their pets.

        Returns:
            A list of all users with their pet information.
        """
        try:
            logger.info("Retrieving all users")
            users = [User(**user_data) for user_data in self._users_data]
            logger.info(f"Successfully retrieved {len(users)} users")
            return users
        except Exception as e:
            logger.error(f"Error retrieving users: {e}", exc_info=True)
            raise

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Retrieves a specific user by their ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            The user data if found, None otherwise.

        Raises:
            ValueError: If the user_id is not a positive integer.
            UserNotFoundError: If the user is not found.
        """
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer")

        try:
            logger.info(f"Retrieving user with ID: {user_id}")

            for user_data in self._users_data:
                if user_data["id"] == user_id:
                    user = User(**user_data)
                    logger.info(f"Successfully retrieved user {user_id}")
                    return user

            logger.warning(f"User with ID {user_id} not found")
            raise UserNotFoundError(f"User with ID {user_id} not found")

        except UserNotFoundError:
            raise
        except Exception as e:
            logger.error(f"Error retrieving user {user_id}: {e}", exc_info=True)
            raise

    def get_users_by_pet_species(self, species: str) -> List[User]:
        """
        Retrieves users who own pets of a specific species.

        Args:
            species: The species to filter by.

        Returns:
            A list of users who own pets of the specified species.
        """
        try:
            logger.info(f"Retrieving users with pets of species: {species}")

            matching_users = []
            for user_data in self._users_data:
                user_pets = user_data.get("pets", [])
                if any(pet["species"].lower() == species.lower() for pet in user_pets):
                    matching_users.append(User(**user_data))

            logger.info(f"Found {len(matching_users)} users with {species} pets")
            return matching_users

        except Exception as e:
            logger.error(f"Error filtering users by pet species {species}: {e}", exc_info=True)
            raise

    def _get_mock_data(self) -> List[Dict[str, Any]]:
        """
        Returns mock data for users and their pets.

        Returns:
            A list of user dictionaries with pet information.
        """
        return [
            {
                "id": 1,
                "name": "Alice Johnson",
                "email": "alice.johnson@example.com",
                "age": 28,
                "created_at": datetime(2023, 1, 15, 10, 30, 0),
                "pets": [
                    {
                        "id": 1,
                        "name": "Buddy",
                        "species": "dog",
                        "breed": "Golden Retriever",
                        "age": 3
                    },
                    {
                        "id": 2,
                        "name": "Whiskers",
                        "species": "cat",
                        "breed": "Persian",
                        "age": 2
                    }
                ]
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "email": "bob.smith@example.com",
                "age": 35,
                "created_at": datetime(2023, 2, 20, 14, 45, 0),
                "pets": [
                    {
                        "id": 3,
                        "name": "Chirpy",
                        "species": "bird",
                        "breed": "Canary",
                        "age": 1
                    }
                ]
            },
            {
                "id": 3,
                "name": "Carol Williams",
                "email": "carol.williams@example.com",
                "age": 42,
                "created_at": datetime(2023, 3, 10, 9, 15, 0),
                "pets": [
                    {
                        "id": 4,
                        "name": "Max",
                        "species": "dog",
                        "breed": "German Shepherd",
                        "age": 5
                    },
                    {
                        "id": 5,
                        "name": "Luna",
                        "species": "cat",
                        "breed": "Siamese",
                        "age": 3
                    },
                    {
                        "id": 6,
                        "name": "Goldie",
                        "species": "fish",
                        "breed": "Goldfish",
                        "age": 1
                    }
                ]
            },
            {
                "id": 4,
                "name": "David Brown",
                "email": "david.brown@example.com",
                "age": 29,
                "created_at": datetime(2023, 4, 5, 16, 20, 0),
                "pets": []
            },
            {
                "id": 5,
                "name": "Emma Davis",
                "email": "emma.davis@example.com",
                "age": 31,
                "created_at": datetime(2023, 5, 12, 11, 0, 0),
                "pets": [
                    {
                        "id": 7,
                        "name": "Rocky",
                        "species": "dog",
                        "breed": "Bulldog",
                        "age": 4
                    }
                ]
            }
        ]
