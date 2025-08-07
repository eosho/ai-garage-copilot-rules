---
description: "Guidelines for writing Python classes."
applyTo: "**/*.py"
---

# Python Class Instructions

## Class Design

- **Single Responsibility Principle**: A class should have one, and only one, reason to change.
- **Cohesion**: Keep related data and methods together in the same class.
- **Inheritance**: Use inheritance to model "is-a" relationships. Prefer composition over inheritance where possible.
- **Data Classes**: Use `@dataclass` for classes that are primarily used to store data.

## Methods

- **`__init__`**: Keep the `__init__` method simple. It should only initialize the object's state.
- **Method Size**: Keep methods small and focused on a single task.
- **`@classmethod`**: Use for methods that operate on the class itself, not an instance.
- **`@staticmethod`**: Use for utility functions that are related to the class but don't need access to the class or instance.

## Example

```python
from dataclasses import dataclass
from typing import Type

@dataclass
class UserProfile:
    """A data class for user profile information."""
    name: str
    email: str
    age: int

class UserAccount:
    """Manages a user's account and profile."""

    def __init__(self, user_id: int, profile: UserProfile):
        """
        Initializes the UserAccount.

        Args:
            user_id: The unique identifier for the user.
            profile: A UserProfile data class instance.
        """
        self.user_id = user_id
        self.profile = profile
        self._is_active = True

    def deactivate(self) -> None:
        """Deactivates the user's account."""
        self._is_active = False

    @classmethod
    def create_guest_account(cls: Type['UserAccount']) -> 'UserAccount':
        """
        Creates a guest user account.

        Returns:
            A new UserAccount instance for a guest user.
        """
        guest_profile = UserProfile(name="Guest", email="", age=0)
        return cls(user_id=0, profile=guest_profile)

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates an email address format.

        Args:
            email: The email string to validate.

        Returns:
            True if the email format is valid, False otherwise.
        """
        return "@" in email and "." in email.split("@")[-1]
```
