FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create non-root user for security
RUN groupadd -r weatherapp && useradd -r -g weatherapp weatherapp

# Set work directory
WORKDIR /app

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv sync --frozen --no-cache --no-dev

# Copy application code
COPY . .

# Change ownership to non-root user
RUN chown -R weatherapp:weatherapp /app

# Switch to non-root user
USER weatherapp

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["uv", "run", "uvicorn", "weather_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
