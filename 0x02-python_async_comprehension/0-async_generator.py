#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no argument
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
