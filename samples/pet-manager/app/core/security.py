"""Security utilities for authentication and authorization."""

import logging
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from .config import settings

logger = logging.getLogger(__name__)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT token security
security = HTTPBearer()


class SecurityUtils:
    """Utility class for security operations."""

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verifies a plain password against a hashed password.

        Args:
            plain_password: The plain text password to verify.
            hashed_password: The hashed password to verify against.

        Returns:
            True if the password is valid, False otherwise.
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        Hashes a plain text password.

        Args:
            password: The plain text password to hash.

        Returns:
            The hashed password.
        """
        return pwd_context.hash(password)

    @staticmethod
    def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
        """
        Creates a JWT access token.

        Args:
            data: The data to encode in the token.
            expires_delta: Optional expiration time delta.

        Returns:
            The encoded JWT token.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> Optional[Dict[str, Any]]:
        """
        Verifies and decodes a JWT token.

        Args:
            token: The JWT token to verify.

        Returns:
            The decoded token payload if valid, None otherwise.

        Raises:
            HTTPException: If the token is invalid or expired.
        """
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            return payload
        except JWTError as e:
            logger.warning(f"JWT verification failed: {e}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )


def get_current_user(token: str = Depends(security)) -> Dict[str, Any]:
    """
    Dependency to get the current authenticated user from JWT token.

    Args:
        token: The JWT token from the Authorization header.

    Returns:
        The current user information.

    Raises:
        HTTPException: If the token is invalid or user not found.
    """
    payload = SecurityUtils.verify_token(token.credentials)
    user_id: str = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    # In a real application, you would fetch the user from the database
    # For this example, we'll return a mock user
    return {"user_id": user_id, "username": payload.get("username")}
