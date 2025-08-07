---
description: "Guidelines for logging in Python applications."
applyTo: "**/*.py"
---

# Python Logging Instructions

## General Principles

- **Structured Logging**: Use structured logging (e.g., JSON format) to make logs easier to parse and analyze.
- **Log Levels**: Use appropriate log levels:
  - `DEBUG`: Detailed information, typically of interest only when diagnosing problems.
  - `INFO`: Confirmation that things are working as expected.
  - `WARNING`: An indication that something unexpected happened, or indicative of some problem in the near future.
  - `ERROR`: Due to a more serious problem, the software has not been able to perform some function.
  - `CRITICAL`: A serious error, indicating that the program itself may be unable to continue running.
- **Context**: Include relevant context in your log messages (e.g., user ID, request ID).
- **Configuration**: Configure logging in a central place, preferably from a configuration file.

## Example

```python
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def process_request(request_id: str, user_id: int):
    """Processes an incoming request."""
    logger.info(
        "Processing request",
        extra={"request_id": request_id, "user_id": user_id}
    )
    try:
        # ... processing logic ...
        logger.info("Request processed successfully", extra={"request_id": request_id})
    except Exception as e:
        logger.error(
            "Failed to process request",
            exc_info=True,
            extra={"request_id": request_id}
        )
```
