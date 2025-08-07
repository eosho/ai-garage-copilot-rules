---
description: "Guidelines for optimizing performance in Python 3.10+ applications, including concurrency patterns, caching strategies, and memory optimization."
applyTo: "**/*.py"
---

# Python Performance Optimization Instructions

## General Performance Principles

- **Profile First**: Always measure before optimizing. Use `cProfile`, `py-spy`, or `line_profiler`.
- **Bottleneck Focus**: Optimize the actual bottlenecks, not perceived slow areas.
- **Readability vs Performance**: Don't sacrifice code clarity for micro-optimizations.
- **Modern Python**: Leverage Python 3.10+ features like structural pattern matching and improved typing.

## Concurrency Patterns

### **When to Use Async vs Sync**

**Use Async For:**
- **I/O Operations**: Database queries, API calls, file operations, network requests
- **Concurrent Processing**: When you need to handle multiple operations simultaneously
- **Web Frameworks**: FastAPI, aiohttp, and other async web frameworks
- **Long-Running Operations**: Tasks that involve waiting (timeouts, polling)

**Avoid Async For:**
- **CPU-Intensive Tasks**: Mathematical calculations, data processing, encryption
- **Simple Synchronous Operations**: Basic string manipulation, local calculations
- **Legacy Library Integration**: When working with sync-only libraries
- **Quick Scripts**: Simple one-off scripts without I/O operations

### **Async/Await for I/O-Bound Operations**

```python
import asyncio
import aiohttp
from typing import List, Dict, Any

async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """
    Efficiently fetch multiple URLs concurrently.

    Args:
        urls: List of URLs to fetch.

    Returns:
        List of response data.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_single_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    return [result for result in results if isinstance(result, dict)]

async def fetch_single_url(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """
    Fetch a single URL with error handling and timeout.

    Args:
        session: Async HTTP client session.
        url: URL to fetch data from.

    Returns:
        JSON response data as dictionary, or empty dict on error.
    """
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            return await response.json()
    except asyncio.TimeoutError:
        logger.warning(f"Timeout fetching {url}")
        return {}
    except Exception as e:
        logger.warning(f"Failed to fetch {url}: {e}")
        return {}

async def batch_with_concurrency_control(items: List[str]) -> List[Dict[str, Any]]:
    """
    Process items with controlled concurrency and error handling.

    Args:
        items: Items to process.

    Returns:
        List of successful results.
    """
    semaphore = asyncio.Semaphore(10)  # Limit concurrent operations

    async def process_item(item: str) -> Optional[Dict[str, Any]]:
        """
        Process a single item with timeout and error handling.

        Args:
            item: Item to process.

        Returns:
            Processed result or None if processing failed.
        """
        async with semaphore:
            try:
                return await asyncio.wait_for(
                    expensive_async_operation(item),
                    timeout=30.0
                )
            except (asyncio.TimeoutError, Exception) as e:
                logger.warning(f"Failed to process {item}: {e}")
                return None

    tasks = [process_item(item) for item in items]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    return [result for result in results if isinstance(result, dict)]
```

### **ThreadPoolExecutor for CPU-Bound Tasks**

```python
import concurrent.futures
from typing import List, Callable, Any

def process_cpu_intensive_tasks(
    items: List[Any],
    processor: Callable[[Any], Any],
    max_workers: int = None
) -> List[Any]:
    """
    Process CPU-intensive tasks using thread pool.

    Args:
        items: Items to process.
        processor: Function to process each item.
        max_workers: Maximum number of worker threads.

    Returns:
        List of processed results.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(processor, item) for item in items]
        results = []

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                logger.error(f"Task failed: {e}")

    return results

### **FastAPI Async Patterns**

```python
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_async_db)
) -> UserResponse:
    """
    Efficiently retrieve a user with async database operation.

    Args:
        user_id: The user's unique identifier.
        db: Async database session.

    Returns:
        User data.

    Raises:
        HTTPException: If user is not found.
    """
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.from_orm(user)

@app.post("/users/batch")
async def create_users_batch(
    users_data: List[UserCreate],
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_async_db)
) -> List[UserResponse]:
    """
    Create multiple users concurrently with background processing.

    Args:
        users_data: List of user creation data.
        background_tasks: Background task manager.
        db: Async database session.

    Returns:
        List of created users.
    """
    # Create users concurrently
    tasks = [create_user(db, user_data) for user_data in users_data]
    users = await asyncio.gather(*tasks)

    # Schedule background tasks (email notifications, etc.)
    for user in users:
        background_tasks.add_task(send_welcome_email, user.email)

    return [UserResponse.from_orm(user) for user in users]

async def mixed_async_sync_processing(user_id: int) -> Dict[str, Any]:
    """
    Example of efficiently mixing async I/O and sync calculations.

    Args:
        user_id: User identifier.

    Returns:
        Processed user data.
    """
    # Async I/O operation
    user_data = await fetch_user_data(user_id)

    # Sync data transformation (don't make this async)
    formatted_name = f"{user_data['first_name']} {user_data['last_name']}".title()
    calculated_score = calculate_user_score(user_data)  # CPU-intensive, keep sync

    return {
        **user_data,
        "formatted_name": formatted_name,
        "score": calculated_score
    }
```
```

## Caching Strategies

### **Function-Level Caching**

```python
from functools import lru_cache, cache
from typing import List, Dict
import time

@lru_cache(maxsize=128)
def expensive_calculation(n: int) -> int:
    """
    Expensive calculation with LRU cache.

    Args:
        n: Input parameter.

    Returns:
        Calculated result.
    """
    # Simulate expensive operation
    time.sleep(0.1)
    return n ** 2 + n

@cache  # Python 3.9+ - unbounded cache
def get_static_config(config_type: str) -> Dict[str, Any]:
    """
    Get static configuration with unbounded cache.

    Args:
        config_type: Type of configuration to retrieve.

    Returns:
        Configuration dictionary.
    """
    # Expensive config loading operation
    return load_config_from_file(config_type)
```

### **Redis Caching with TTL**

```python
import redis
import json
import pickle
from typing import Any, Optional
from datetime import timedelta

class RedisCache:
    """Redis-based caching with TTL support."""

    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_client = redis.from_url(redis_url)

    async def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache.

        Args:
            key: Cache key.

        Returns:
            Cached value or None if not found.
        """
        try:
            value = await self.redis_client.get(key)
            return pickle.loads(value) if value else None
        except Exception as e:
            logger.warning(f"Cache get failed for {key}: {e}")
            return None

    async def set(self, key: str, value: Any, ttl: timedelta = timedelta(hours=1)) -> bool:
        """
        Set value in cache with TTL.

        Args:
            key: Cache key.
            value: Value to cache.
            ttl: Time to live.

        Returns:
            True if successful, False otherwise.
        """
        try:
            serialized = pickle.dumps(value)
            await self.redis_client.setex(key, ttl, serialized)
            return True
        except Exception as e:
            logger.error(f"Cache set failed for {key}: {e}")
            return False

# Usage with decorator
def cached_db_query(cache: RedisCache, ttl: timedelta = timedelta(minutes=30)):
    """
    Decorator for caching database queries with Redis.

    Args:
        cache: Redis cache instance.
        ttl: Time to live for cached results.

    Returns:
        Decorator function that caches the wrapped function's results.
    """
    def decorator(func):
        """
        Inner decorator function.

        Args:
            func: Function to be cached.

        Returns:
            Wrapped function with caching behavior.
        """
        async def wrapper(*args, **kwargs):
            """
            Wrapper function that implements caching logic.

            Args:
                *args: Positional arguments for the wrapped function.
                **kwargs: Keyword arguments for the wrapped function.

            Returns:
                Cached result or fresh result from function execution.
            """
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"

            # Try cache first
            result = await cache.get(cache_key)
            if result is not None:
                return result

            # Execute function and cache result
            result = await func(*args, **kwargs)
            await cache.set(cache_key, result, ttl)
            return result
        return wrapper
    return decorator
```

## Memory Optimization

### **Efficient Data Structures**

```python
from typing import List, Dict, NamedTuple, Union
from dataclasses import dataclass
from collections import deque, defaultdict
import sys

# Use slots for memory-efficient classes
@dataclass
class User:
    """Memory-efficient user representation with slots."""
    __slots__ = ['id', 'email', 'name', 'is_active']

    id: int
    email: str
    name: str
    is_active: bool = True

# Use NamedTuple for immutable data
class Point(NamedTuple):
    """Memory-efficient point representation."""
    x: float
    y: float

    def distance_from_origin(self) -> float:
        """
        Calculate the Euclidean distance from the origin (0, 0).

        Returns:
            Distance from origin as a float.
        """

# Use generators for large datasets
def process_large_file(filename: str):
    """
    Process large file without loading everything into memory.

    Args:
        filename: Path to the file to process.

    Yields:
        Processed line data.
    """
    with open(filename, 'r') as file:
        for line in file:
            # Process line without storing all lines
            yield process_line(line.strip())

# Use deque for efficient append/pop operations
class CircularBuffer:
    """Memory-efficient circular buffer using deque."""

    def __init__(self, maxsize: int):
        """
        Initialize the circular buffer.

        Args:
            maxsize: Maximum number of items to store in the buffer.
        """
        self.buffer = deque(maxlen=maxsize)

    def add(self, item: Any) -> None:
        """
        Add item to buffer (automatically removes oldest if full).

        Args:
            item: Item to add to the buffer.
        """
        self.buffer.append(item)

    def get_recent(self, n: int) -> List[Any]:
        """
        Get n most recent items from the buffer.

        Args:
            n: Number of recent items to retrieve.

        Returns:
            List of the n most recent items.
        """
        return list(self.buffer)[-n:]
```

### **Memory Profiling and Monitoring**

```python
import tracemalloc
import psutil
import os
from typing import Dict, Any

def memory_profiler(func):
    """
    Decorator to profile memory usage of a function.

    Args:
        func: Function to be profiled for memory usage.

    Returns:
        Wrapped function that logs memory usage statistics.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that implements memory profiling.

        Args:
            *args: Positional arguments for the wrapped function.
            **kwargs: Keyword arguments for the wrapped function.

        Returns:
            Result from the wrapped function execution.
        """
        tracemalloc.start()

        # Get initial memory
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB

        try:
            result = func(*args, **kwargs)

            # Get final memory and tracemalloc stats
            current, peak = tracemalloc.get_traced_memory()
            final_memory = process.memory_info().rss / 1024 / 1024  # MB

            logger.info(
                f"Function {func.__name__} memory usage: "
                f"Process: {initial_memory:.1f}MB -> {final_memory:.1f}MB "
                f"(+{final_memory - initial_memory:.1f}MB), "
                f"Traced: Current {current / 1024 / 1024:.1f}MB, "
                f"Peak {peak / 1024 / 1024:.1f}MB"
            )

            return result
        finally:
            tracemalloc.stop()

    return wrapper

@memory_profiler
async def process_large_dataset(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Example function with memory profiling for processing large datasets.

    Args:
        data: List of data dictionaries to process.

    Returns:
        List of transformed data items.
    """
    # Process data efficiently
    return [transform_item(item) for item in data]
```

## Database Performance

### **Efficient SQLAlchemy Patterns**

```python
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from typing import List, Optional

async def get_users_with_posts_efficient(
    db: AsyncSession,
    limit: int = 100
) -> List[User]:
    """
    Efficiently load users with their posts using selectinload.

    Args:
        db: Database session.
        limit: Maximum number of users to return.

    Returns:
        List of users with loaded posts.
    """
    result = await db.execute(
        select(User)
        .options(selectinload(User.posts))  # Efficient N+1 prevention
        .limit(limit)
    )
    return result.scalars().all()

async def get_user_stats_batch(
    db: AsyncSession,
    user_ids: List[int]
) -> Dict[int, Dict[str, int]]:
    """
    Get user statistics in a single query.

    Args:
        db: Database session.
        user_ids: List of user IDs.

    Returns:
        Dictionary mapping user ID to stats.
    """
    result = await db.execute(
        select(
            User.id,
            func.count(Post.id).label('post_count'),
            func.count(Comment.id).label('comment_count')
        )
        .outerjoin(Post)
        .outerjoin(Comment)
        .where(User.id.in_(user_ids))
        .group_by(User.id)
    )

    return {
        row.id: {
            'post_count': row.post_count,
            'comment_count': row.comment_count
        }
        for row in result
    }
```

## Algorithm Optimization

### **Efficient Algorithms and Data Structures**

```python
from typing import List, Set, Dict, Any
from collections import Counter, defaultdict
import bisect

def find_duplicates_efficient(items: List[Any]) -> Set[Any]:
    """
    Find duplicates using Counter (O(n) time complexity).

    Args:
        items: List of items to check for duplicates.

    Returns:
        Set of duplicate items.
    """
    counts = Counter(items)
    return {item for item, count in counts.items() if count > 1}

def binary_search_insert(sorted_list: List[int], value: int) -> int:
    """
    Efficiently insert value into sorted list maintaining order.

    Args:
        sorted_list: Already sorted list.
        value: Value to insert.

    Returns:
        Index where value was inserted.
    """
    index = bisect.bisect_left(sorted_list, value)
    sorted_list.insert(index, value)
    return index

class LRUCache:
    """
    Efficient LRU cache implementation using OrderedDict.
    Better than functools.lru_cache for custom eviction logic.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache.

        Args:
            capacity: Maximum number of items to store in the cache.
        """
        self.capacity = capacity
        self.cache: Dict[Any, Any] = {}
        self.access_order: List[Any] = []

    def get(self, key: Any) -> Optional[Any]:
        """
        Get value from cache and update access order.

        Args:
            key: Key to retrieve from cache.

        Returns:
            Cached value or None if key not found.
        """
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None

    def put(self, key: Any, value: Any) -> None:
        """
        Put value in cache and handle eviction if necessary.

        Args:
            key: Key to store the value under.
            value: Value to store in the cache.
        """
        if key in self.cache:
            self.access_order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Evict least recently used
            lru_key = self.access_order.pop(0)
            del self.cache[lru_key]

        self.cache[key] = value
        self.access_order.append(key)
```

## Performance Monitoring

### **Application Performance Monitoring**

```python
import time
import functools
from typing import Callable, Any
from contextlib import contextmanager

class PerformanceMonitor:
    """Performance monitoring and metrics collection."""

    def __init__(self):
        """
        Initialize the performance monitor.

        Creates an empty metrics dictionary to store timing data
        for different operations.
        """
        self.metrics: Dict[str, List[float]] = defaultdict(list)

    def timing_decorator(self, operation_name: str):
        """
        Decorator to measure function execution time.

        Args:
            operation_name: Name to identify the operation being timed.

        Returns:
            Decorator function that measures execution time of the wrapped function.
        """
        def decorator(func: Callable) -> Callable:
            """
            Inner decorator that creates timing wrappers.

            Args:
                func: Function to be wrapped with timing functionality.

            Returns:
                Async or sync wrapper depending on the function type.
            """
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                """
                Async wrapper that measures execution time.

                Args:
                    *args: Positional arguments for the wrapped function.
                    **kwargs: Keyword arguments for the wrapped function.

                Returns:
                    Result from the wrapped async function.
                """
                start_time = time.perf_counter()
                try:
                    result = await func(*args, **kwargs)
                    return result
                finally:
                    execution_time = time.perf_counter() - start_time
                    self.metrics[operation_name].append(execution_time)

                    if execution_time > 1.0:  # Log slow operations
                        logger.warning(
                            f"Slow operation {operation_name}: {execution_time:.2f}s"
                        )

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                """
                Sync wrapper that measures execution time.

                Args:
                    *args: Positional arguments for the wrapped function.
                    **kwargs: Keyword arguments for the wrapped function.

                Returns:
                    Result from the wrapped sync function.
                """
                start_time = time.perf_counter()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    execution_time = time.perf_counter() - start_time
                    self.metrics[operation_name].append(execution_time)

            return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
        return decorator

    @contextmanager
    def measure(self, operation_name: str):
        """
        Context manager for measuring execution time of code blocks.

        Args:
            operation_name: Name to identify the operation being measured.

        Yields:
            None - allows code execution within the context.
        """
        start_time = time.perf_counter()
        try:
            yield
        finally:
            execution_time = time.perf_counter() - start_time
            self.metrics[operation_name].append(execution_time)

    def get_stats(self, operation_name: str) -> Dict[str, float]:
        """
        Get performance statistics for a specific operation.

        Args:
            operation_name: Name of the operation to get statistics for.

        Returns:
            Dictionary containing performance statistics including count,
            total time, average, min, max, and 95th percentile.
        """
        times = self.metrics[operation_name]
        if not times:
            return {}

        return {
            'count': len(times),
            'total': sum(times),
            'average': sum(times) / len(times),
            'min': min(times),
            'max': max(times),
            'p95': sorted(times)[int(len(times) * 0.95)] if times else 0
        }

# Global performance monitor instance
perf_monitor = PerformanceMonitor()

# Usage examples
@perf_monitor.timing_decorator("database_query")
async def fetch_user_data(user_id: int) -> Dict[str, Any]:
    """
    Fetch user data with comprehensive performance monitoring.

    This function demonstrates how to use performance monitoring
    for both cache checks and database operations.

    Args:
        user_id: Unique identifier of the user to fetch.

    Returns:
        Dictionary containing user data, or empty dict if not found.
    """
    with perf_monitor.measure("cache_check"):
        cached = await cache.get(f"user:{user_id}")

    if cached:
        return cached

    with perf_monitor.measure("database_query_execution"):
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

    return user.to_dict() if user else {}
```
