---
description: "Guidelines for writing Python functions."
applyTo: "**/*.py"
---

# Python Function Instructions

## Function Design

- **Single Responsibility**: A function should do one thing and do it well.
- **Pure Functions**: Prefer pure functions (functions that have no side effects and always return the same output for the same input).
- **Argument Count**: Aim for a small number of arguments. If you have more than 3-4, consider using a data class or dictionary.
- **Default Arguments**: Use default arguments to make functions more flexible. Avoid using mutable objects as default arguments.

## Return Values

- **Consistency**: A function should always return a value of the same type.
- **Multiple Values**: Use tuples to return multiple values.
- **Clarity**: Be explicit about what your function returns.

## Example

```python
from typing import Tuple, Optional, List, Dict, Any

def calculate_order_total(
    items: List[Dict[str, Any]],
    discount: float = 0.0,
    tax_rate: float = 0.0
) -> float:
    """Calculates the total cost of an order.

    Args:
        items: A list of item dictionaries, each with a 'price' key.
        discount: The discount percentage to apply.
        tax_rate: The tax rate to apply.

    Returns:
        The final total cost of the order.
    """
    subtotal = sum(item.get('price', 0) for item in items)
    discounted_total = subtotal * (1 - discount)
    final_total = discounted_total * (1 + tax_rate)
    return final_total

def parse_user_input(input_str: str) -> Tuple[str, Optional[int]]:
    """Parses user input into a command and an optional value.

    Args:
        input_str: The raw string input from the user.

    Returns:
        A tuple containing the command and an optional integer value.
    """
    parts = input_str.split()
    command = parts[0]
    value = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
    return command, value
```
