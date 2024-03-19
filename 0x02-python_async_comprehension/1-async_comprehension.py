#!/usr/bin/env python3
"""
Imports async function from the previous task
writes a co-routine ca;lled async_comprehension
"""
import asyncio
from typing import List
generated = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect ten rando numbers using async comprehension"""
    return ([i async for i in generated()])
