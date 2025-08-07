---
description: "Guidelines for production-grade logging in Python applications with OpenTelemetry."
applyTo: "**/*.py"
---

# Python Logging Instructions

## General Principles

- **OpenTelemetry Integration**: Use OpenTelemetry for unified logging, tracing, and metrics collection.
- **Cloud-Native**: Support modern observability platforms like Azure App Insights while remaining vendor-neutral.
- **Structured Logging**: Use JSON format for machine-readable logs that are easy to query and analyze.
- **Log Levels**:
  - `DEBUG`: Detailed diagnostic information for development
  - `INFO`: Confirmation that things are working as expected
  - `WARNING`: Unexpected events that don't cause operation failures
  - `ERROR`: Operation failures that need attention
  - `CRITICAL`: Severe errors affecting the entire application
- **Context**: Always include correlation IDs (trace ID, request ID) and relevant business context.
- **Configuration**: Use environment variables or config files for logging settings.

## Example

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
import logging
import json
import sys
from typing import Optional

def setup_logging(log_to_file: bool = False) -> None:
    """
    Configure structured logging with OpenTelemetry and optional file output.

    Args:
        log_to_file: Whether to enable logging to app.log file
    """
    # Configure OpenTelemetry (exports to Azure App Insights if connection string exists)
    provider = TracerProvider()
    exporter = AzureMonitorTraceExporter()
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    # Custom JSON formatter that includes trace context
    class JsonFormatter(logging.Formatter):
        def format(self, record) -> str:
            """
            Format a log record into a structured JSON string with OpenTelemetry context.

            Args:
                record: The LogRecord instance to be formatted.

            Returns:
                A JSON string containing the formatted log record with trace context.
                Includes timestamp, log level, message, trace_id, span_id, and any
                extra data attached to the record.
            """
            span = trace.get_current_span()
            record_dict = {
                "timestamp": self.formatTime(record),
                "level": record.levelname,
                "message": record.getMessage(),
                "trace_id": span.get_span_context().trace_id,
                "span_id": span.get_span_context().span_id,
            }
            if hasattr(record, "extra_data"):
                record_dict.update(record.extra_data)
            return json.dumps(record_dict)

    # Configure handlers
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_to_file:
        handlers.append(logging.FileHandler("app.log"))

    # Apply configuration
    logging.basicConfig(
        level=logging.INFO,
        handlers=handlers,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    for handler in logging.root.handlers:
        handler.setFormatter(JsonFormatter())

# Usage example
logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)

def process_order(order_id: str) -> None:
    """
    Process an order with integrated logging and tracing capabilities.

    This function demonstrates the integration of OpenTelemetry tracing with
    structured logging. It creates a new trace span for the order processing
    operation and logs the progress with correlated trace IDs.

    Args:
        order_id: The unique identifier of the order to process.

    Raises:
        Exception: If order processing fails. The error will be logged with
            full stack trace and correlated trace context.

    Example:
        >>> process_order("ORD-123")
        # Logs:
        # {"timestamp": "2025-08-07 10:00:00", "level": "INFO", "message": "Processing order",
        #  "trace_id": "abc...", "span_id": "def...", "order_id": "ORD-123"}
    """
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order_id", order_id)
        logger.info(
            "Processing order",
            extra={"extra_data": {"order_id": order_id}}
        )
        try:
            # Business logic here
            logger.info(
                "Order processed successfully",
                extra={"extra_data": {"order_id": order_id}}
            )
        except Exception as e:
            logger.error(
                f"Order processing failed: {str(e)}",
                extra={"extra_data": {"order_id": order_id}},
                exc_info=True
            )
```
