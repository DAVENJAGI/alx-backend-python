#!/usr/bin/env python3
""" Async comprenhesion generator that takes no argument.
The coroutine collects 10 random numbers using an async
comprehensing over async_generator
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generate number with async comprenhension
    """
    numbers = ([i async for i in async_generator()])
    return numbers
