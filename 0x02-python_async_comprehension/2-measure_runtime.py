#!/usr/bin/env python3
'''
Import async_comprehension from the previous
file and measure runtime
'''


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure the average runtime'''
    start_time = time.time()
    generator = [async_comprehension() for i in range(4)]
    await asyncio.gather(*generator)
    end_time = time.time()

    tot_time = end_time - start_time
    return tot_time
