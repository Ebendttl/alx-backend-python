import asyncio

async def wait_n(n: int, max_delay: float) -> list[float]:
    """Spawns `n` asynchronous wait operations concurrently using [wait_random](cci:1:///home/ebendttl/ALX/alx-backend-python/0x01-python_async_function/1-concurrent_coroutines.py:16:0-28:16).

    Args:
        n: The number of times to spawn the wait operation.
        max_delay: The maximum delay (in seconds) for each wait operation.

    Returns:
        A list of delays (in seconds) in ascending order, reflecting the completion time of each wait operation. Sorting is not used due to concurrency.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

