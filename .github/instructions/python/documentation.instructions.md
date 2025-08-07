---
description: "Guidelines for documenting Python code."
applyTo: "**/*.py"
---

# Python Documentation Instructions

## Docstring Format

- **Google Style**: Use the Google Python Style Guide for docstrings.
- **Completeness**: All public modules, classes, functions, and methods must have docstrings.
- **Content**: Docstrings should describe what the code does, its arguments (`Args:`), what it returns (`Returns:`), and what it might raise (`Raises:`).

## Example

```python
class UserService:
    """
    Manages user-related operations in the system.

    This class provides methods for creating, retrieving, and updating user
    information. It interacts with the database to persist user data.
    """

    def get_user(self, user_id: int) -> Optional[dict]:
        """
        Retrieves a user by their ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            A dictionary containing the user's data, or None if the user
            is not found.

        Raises:
            ValueError: If the user_id is not a positive integer.
        """
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer.")
        # ... database logic ...
```
