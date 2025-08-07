---
description: "Guidelines for using type hints in Python."
applyTo: "**/*.py"
---

# Python Typing Instructions

## General Principles

- **Type Everything**: Add type hints to all function signatures, including arguments and return values.
- **Be Specific**: Use specific types whenever possible (e.g., `list[int]` instead of `list`).
- **Use `Optional`**: Use `Optional[T]` for values that can be `None`.
- **Use `Union`**: Use `Union[T, U]` for values that can be one of several types.
- **Use `Any` Sparingly**: Only use `Any` when you cannot use a more specific type.

## Example

```python
from typing import List, Dict, Optional, Union, Tuple

def process_data(
    data: List[Dict[str, Union[int, str]]],
    config: Optional[Dict[str, str]] = None
) -> Tuple[int, str]:
    """
    Processes a list of data dictionaries.

    Args:
        data: A list of dictionaries to process.
        config: An optional configuration dictionary.

    Returns:
        A tuple containing the number of processed records and a status message.
    """
    if not config:
        config = {}

    processed_count = 0
    for item in data:
        # ... processing logic ...
        processed_count += 1

    return processed_count, "Success"
```
