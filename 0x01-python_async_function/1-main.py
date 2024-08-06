#!/usr/bin/env python3
"""
This module contains an asynchronous routine that spawns wait_random n times
with the specified max_delay and returns the list of delays.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random  # Changed import statement


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
