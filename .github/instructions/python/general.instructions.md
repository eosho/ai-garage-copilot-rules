---
description: "General Python coding standards and best practices."
applyTo: "**/*.py"
---

# General Python Coding Instructions

**Keywords**: #python #styleguide #pep8 #best-practices

## General Principles

- **Readability Counts**: Write code that is easy to read and understand. Follow PEP 8 guidelines.
- **Explicit is better than implicit**: Be clear and explicit in your code.
- **Simple is better than complex**: Prefer simple, straightforward solutions.
- **Keep it DRY**: Don't Repeat Yourself. Avoid duplicating code.

## Naming Conventions

- **Variables**: Use `snake_case` for variable names (e.g., `user_name`).
- **Functions**: Use `snake_case` for function names (e.g., `calculate_total`).
- **Classes**: Use `PascalCase` for class names (e.g., `UserAccount`).
- **Constants**: Use `UPPER_SNAKE_CASE` for constants (e.g., `MAX_CONNECTIONS`).
- **Modules**: Use short, `snake_case` names for modules.
- **Private Attributes**: Use a leading underscore for internal attributes (e.g., `_internal_state`).

## Code Formatting

- **Indentation**: Use 4 spaces per indentation level.
- **Line Length**: Keep lines under 88 characters (the Black default).
- **Quotes**: Use double quotes `"` for strings, unless a string contains double quotes, in which case use single quotes `'`.
- **Whitespace**: Use whitespace judiciously to improve readability.

## Comments

- **Clarity**: Write clear, concise comments that explain the "why," not the "what."
- **Docstrings**: Use docstrings for all public modules, functions, classes, and methods.
- **TODOs**: Use `TODO` comments to mark areas that need future attention.

## Project Structure

A well-organized project structure is crucial for maintainability and scalability. Here is a recommended structure for a Python application:

```
my_project/
├── my_project/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py
│   └── core/
│       ├── __init__.py
│       └── config.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── pyproject.toml
└── README.md
```

- **`my_project/` (root)**: The main project directory.
- **`my_project/my_project/`**: The main application package.
- **`tests/`**: Contains all the tests.
- **`pyproject.toml`**: For project metadata and dependencies (using Poetry or similar).

To run the application as a module, use:
```bash
python -m my_project.main
```

## Dependency Management

- **Use UV**: Use UV for fast dependency installation and environment management instead of pip.
- **Virtual Environment Requirement**: **ALWAYS** execute Python code in a virtual environment, never directly on the host OS.
- **Environment Detection**: Check for existing `.venv` directory in workspace; create one if it doesn't exist.
- **Explicit Dependencies**: Keep all dependencies explicitly listed in `pyproject.toml` with version constraints.
- **Lock Files**: Commit `uv.lock` files to ensure reproducible builds across environments.
- **Development Dependencies**: Separate development dependencies from runtime dependencies in `pyproject.toml`.

### Virtual Environment Management

When executing Python code, Copilot must:
1. **Check for existing virtual environment**: Look for `.venv` directory in the workspace root
2. **Create if missing**: Use `uv venv` to create `.venv` if it doesn't exist (fallback to `python -m venv .venv` if UV not available)
3. **Activate environment**: Always run Python commands within the virtual environment context
4. **Install dependencies**: Use `uv sync` or `uv pip install` within the virtual environment

### Security and Isolation Benefits

- **System Protection**: Prevents installing packages globally that could affect the host OS
- **Dependency Isolation**: Avoids conflicts between different projects' dependencies
- **Reproducible Builds**: Ensures consistent behavior across development and deployment environments
- **Package Safety**: Contains potentially malicious or incompatible packages within the environment

### UV Installation and Usage

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Initialize a new project with UV
uv init my_project
cd my_project

# Add a dependency
uv add fastapi

# Add a development dependency
uv add --dev pytest black ruff

# Install all dependencies
uv sync

# Run commands in the UV environment
uv run python -m my_project.main
uv run pytest
```

### Virtual Environment Workflow

```bash
# Check for existing .venv directory
if [ ! -d ".venv" ]; then
    # Create virtual environment if it doesn't exist
    uv venv
fi

# Always use uv run to execute Python commands in the virtual environment
uv run python script.py
uv run pytest
uv run black .
uv run mypy .
```

### Fallback Virtual Environment Workflow

```bash
# Check for existing .venv directory
if [ ! -d ".venv" ]; then
    # Create virtual environment using UV if available, fallback to python -m venv
    if command -v uv &> /dev/null; then
        uv venv
    else
        python -m venv .venv
    fi
fi

# Always use uv run to execute Python commands in the virtual environment
uv run python script.py
uv run pytest
uv run black .
uv run mypy .
```

### Example pyproject.toml

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "A sample Python project"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
dependencies = [
    "fastapi>=0.104.0,<1.0.0",
    "pydantic>=2.5.0,<3.0.0",
    "sqlalchemy>=2.0.0,<3.0.0",
]
requires-python = ">=3.10"

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=7.4.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
]
```

## Example

```python
# constants.py
from typing import Any, Dict, Optional

MAX_RETRIES = 3

# user_service.py
class UserService:
    """Manages user-related operations."""

    def __init__(self, db_session: Any):
        self._db = db_session

    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieves a user by their ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            A dictionary with the user data or None if not found.
        """
        # TODO: Add caching to this method
        user_record = self._db.query(user_id)
        return user_record
```
