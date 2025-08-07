---
description: "Guidelines for error handling in Python."
applyTo: "**/*.py"
---

# Python Error Handling Instructions

## General Principles

- **Fail Fast**: Catch errors as early as possible.
- **Specific Exceptions**: Catch specific exceptions, not generic `Exception`.
- **Custom Exceptions**: Create custom exception classes for your application's specific errors.
- **Context Management**: Use `try...finally` or context managers (`with` statement) to ensure resources are cleaned up.
- **Logging**: Log exceptions with stack traces for debugging.

## Example

```python
import logging
from typing import Any, Dict

class UserNotFoundError(Exception):
    """Raised when a user is not found in the database."""
    pass

class DatabaseConnectionError(Exception):
    """Raised when there is an issue connecting to the database."""
    pass

def get_user_profile(user_id: int, db_connection: Any) -> Dict:
    """
    Retrieves a user's profile from the database.

    Args:
        user_id: The ID of the user to retrieve.
        db_connection: The active database connection object.

    Returns:
        A dictionary representing the user's profile.

    Raises:
        UserNotFoundError: If the user is not found.
        DatabaseConnectionError: If there is a database connection issue.
    """
    try:
        user = db_connection.get(user_id)
        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        return user.profile
    except ConnectionError as e:
        logging.error(f"Database connection error: {e}", exc_info=True)
        raise DatabaseConnectionError("Failed to connect to the database.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        raise
```
