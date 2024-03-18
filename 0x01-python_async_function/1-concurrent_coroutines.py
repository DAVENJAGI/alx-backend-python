#!/usr/bin/env python3
"""
Imports wait_random from previous task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """spawn wait_random n times"""
    delays = []
    lst = []

    for x in range(n):
        lsts = wait_random(max_delay)
        lst.append(lsts)

    for lst in asyncio.as_completed((lst)):
        delay = await lst
        delays.append(delay)

    return delays
