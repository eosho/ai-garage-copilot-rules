---
description: "Guidelines for managing imports in Python."
applyTo: "**/*.py"
---

# Python Imports Instructions

## General Principles

- **Order**: Imports should be ordered as follows:
  1.  Standard library imports (e.g., `os`, `sys`).
  2.  Third-party library imports (e.g., `fastapi`, `sqlalchemy`).
  3.  Local application/library specific imports.
- **Grouping**: Separate each group of imports with a blank line.
- **`isort`**: Use the `isort` tool to automatically format imports.
- **Absolute Imports**: Prefer absolute imports over relative imports.

## Example

```python
# Standard library imports
import json
from pathlib import Path

# Third-party imports
from fastapi import FastAPI
from pydantic import BaseModel

# Local application imports
from .database import engine
from .routers import users, items
```
