---
description: "Guidelines for testing Python applications with pytest."
applyTo: "**/test_*.py,**/*_test.py,**/tests/**/*.py"
---

# Python Testing Instructions

## General Principles

- **`pytest`**: Use the `pytest` framework for all tests.
- **AAA Pattern**: Structure tests using the Arrange-Act-Assert pattern.
- **Test Coverage**: Aim for high test coverage (>80%), especially for critical business logic.
- **Mocking**: Use `unittest.mock` to mock external dependencies in unit tests.
- **Fixtures**: Use `pytest` fixtures for test setup and teardown.

## Example

```python
import pytest
from unittest.mock import Mock

from my_app.services import UserService

@pytest.fixture
def mock_db_session():
    """Fixture for a mocked database session."""
    mock = Mock()
    mock.get_user.return_value = {"id": 1, "name": "Test User"}
    return mock

def test_get_user_success(mock_db_session):
    """
    Tests successful user retrieval.
    """
    # Arrange
    user_service = UserService(db_session=mock_db_session)
    user_id = 1

    # Act
    user = user_service.get_user(user_id)

    # Assert
    assert user is not None
    assert user["id"] == user_id
    mock_db_session.get_user.assert_called_once_with(user_id)

@pytest.mark.parametrize("user_id, expected_exception", [
    (-1, ValueError),
    ("abc", TypeError),
])
def test_get_user_invalid_id(user_id, expected_exception):
    """
    Tests user retrieval with invalid IDs.
    """
    # Arrange
    user_service = UserService(db_session=Mock())

    # Act & Assert
    with pytest.raises(expected_exception):
        user_service.get_user(user_id)
```
