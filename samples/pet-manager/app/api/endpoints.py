"""API endpoints for the users and pets application."""

import logging
from datetime import datetime
from typing import List, Optional

from core.config import settings
from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from models.schemas import (
    ErrorResponse,
    HealthCheck,
    User,
    UserDetailResponse,
    UserResponse,
)
from services.user_service import UserNotFoundError, UserService

logger = logging.getLogger(__name__)

# Create router with prefix
router = APIRouter(prefix=settings.api_v1_prefix, tags=["users"])

# Dependency to get user service
def get_user_service() -> UserService:
    """
    Dependency to get the user service instance.

    Returns:
        An instance of UserService.
    """
    return UserService()


@router.get("/health", response_model=HealthCheck, status_code=status.HTTP_200_OK)
async def health_check() -> HealthCheck:
    """
    Health check endpoint to verify the API is running.

    Returns:
        Health status information.
    """
    logger.info("Health check requested")
    return HealthCheck(
        status="healthy",
        timestamp=datetime.utcnow(),
        version=settings.version
    )


@router.get(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    description="Retrieve a list of all users with their pets information.",
    responses={
        200: {"description": "Successfully retrieved users"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
async def get_users(
    species: Optional[str] = Query(
        None,
        description="Filter users by pet species (e.g., dog, cat, bird)"
    ),
    user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    """
    Retrieve all users with their pets.

    Args:
        species: Optional filter to get users with pets of specific species.
        user_service: The user service dependency.

    Returns:
        A response containing the list of users and their pets.

    Raises:
        HTTPException: If there's an error retrieving the users.
    """
    try:
        logger.info(f"Getting users with species filter: {species}")

        if species:
            users = user_service.get_users_by_pet_species(species)
            message = f"Successfully retrieved users with {species} pets"
        else:
            users = user_service.get_all_users()
            message = "Successfully retrieved all users"

        logger.info(f"Retrieved {len(users)} users")

        return UserResponse(
            success=True,
            data=users,
            message=message
        )

    except Exception as e:
        logger.error(f"Error retrieving users: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving users"
        )


@router.get(
    "/users/{user_id}",
    response_model=UserDetailResponse,
    status_code=status.HTTP_200_OK,
    summary="Get user by ID",
    description="Retrieve a specific user by their ID with their pets information.",
    responses={
        200: {"description": "Successfully retrieved user"},
        400: {"model": ErrorResponse, "description": "Invalid user ID"},
        404: {"model": ErrorResponse, "description": "User not found"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
async def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
) -> UserDetailResponse:
    """
    Retrieve a specific user by their ID.

    Args:
        user_id: The ID of the user to retrieve.
        user_service: The user service dependency.

    Returns:
        A response containing the user and their pets.

    Raises:
        HTTPException: If the user is not found or there's a validation error.
    """
    try:
        logger.info(f"Getting user with ID: {user_id}")

        user = user_service.get_user_by_id(user_id)

        return UserDetailResponse(
            success=True,
            data=user,
            message=f"Successfully retrieved user {user_id}"
        )

    except ValueError as e:
        logger.warning(f"Invalid user ID {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except UserNotFoundError as e:
        logger.warning(f"User {user_id} not found: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error retrieving user {user_id}: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving the user"
        )


# Additional endpoint for getting users with specific pet count
@router.get(
    "/users/stats/pet-count",
    response_model=dict,
    status_code=status.HTTP_200_OK,
    summary="Get user statistics by pet count",
    description="Get statistics about users grouped by their pet count.",
    responses={
        200: {"description": "Successfully retrieved statistics"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
async def get_user_pet_statistics(
    user_service: UserService = Depends(get_user_service)
) -> dict:
    """
    Get statistics about users and their pet counts.

    Args:
        user_service: The user service dependency.

    Returns:
        A dictionary containing pet count statistics.

    Raises:
        HTTPException: If there's an error calculating statistics.
    """
    try:
        logger.info("Calculating user pet statistics")

        users = user_service.get_all_users()

        stats = {
            "total_users": len(users),
            "total_pets": sum(len(user.pets) for user in users),
            "users_with_no_pets": len([user for user in users if not user.pets]),
            "users_with_pets": len([user for user in users if user.pets]),
            "average_pets_per_user": round(
                sum(len(user.pets) for user in users) / len(users) if users else 0, 2
            ),
            "pet_species_count": {}
        }

        # Count pets by species
        species_count = {}
        for user in users:
            for pet in user.pets:
                species_count[pet.species] = species_count.get(pet.species, 0) + 1

        stats["pet_species_count"] = species_count

        logger.info("Successfully calculated user pet statistics")
        return {
            "success": True,
            "data": stats,
            "message": "Successfully calculated user pet statistics"
        }

    except Exception as e:
        logger.error(f"Error calculating user pet statistics: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while calculating statistics"
        )
