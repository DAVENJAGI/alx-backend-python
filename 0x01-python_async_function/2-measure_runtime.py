#!/usr/bin/env python3
"""
Imports wait_n from previous task,
and calculates the avearage waited time
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """spawn wait_random n times with specified max delay"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    tot_time = end_time - start_time
    return (tot_time/n)
