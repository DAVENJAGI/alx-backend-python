#!/usr/bin/env python3
"""
asynchronous coroutine task 1 that awaits
for a random delay between 0 and default max_delay
"""


import random
import asyncio


async def wait_random(max_delay: int = 10.0) -> float:
    """
    An async co-routine that awaits for random delay btwn 0 and max_delay
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
