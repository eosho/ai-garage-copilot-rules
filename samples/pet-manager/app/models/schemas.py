"""Pydantic models and schemas for API requests and responses."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class PetBase(BaseModel):
    """Base schema for pet information."""

    name: str = Field(..., min_length=1, max_length=100, description="The name of the pet")
    species: str = Field(..., min_length=1, max_length=50, description="The species of the pet (e.g., dog, cat, bird)")
    breed: Optional[str] = Field(None, max_length=100, description="The breed of the pet")
    age: Optional[int] = Field(None, ge=0, le=50, description="The age of the pet in years")


class Pet(PetBase):
    """Complete pet schema with ID."""

    id: int = Field(..., description="Unique identifier for the pet")

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    """Base schema for user information."""

    name: str = Field(..., min_length=1, max_length=100, description="The full name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    age: Optional[int] = Field(None, ge=0, le=150, description="The age of the user")


class User(UserBase):
    """Complete user schema with ID and pets."""

    id: int = Field(..., description="Unique identifier for the user")
    pets: List[Pet] = Field(default=[], description="List of pets owned by the user")
    created_at: datetime = Field(..., description="When the user was created")

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    """Response schema for user operations."""

    success: bool = Field(..., description="Whether the operation was successful")
    data: List[User] = Field(..., description="List of users")
    message: str = Field(..., description="Response message")


class UserDetailResponse(BaseModel):
    """Response schema for single user operations."""

    success: bool = Field(..., description="Whether the operation was successful")
    data: Optional[User] = Field(None, description="User data")
    message: str = Field(..., description="Response message")


class HealthCheck(BaseModel):
    """Health check response schema."""

    status: str = Field(..., description="Health status")
    timestamp: datetime = Field(..., description="Current timestamp")
    version: str = Field(..., description="API version")


class ErrorResponse(BaseModel):
    """Error response schema."""

    success: bool = Field(default=False, description="Whether the operation was successful")
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
