#!/usr/bin/env python3
"""
A function that takes an intger max_delay and returns asyncio.Task
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns asycio.TAsk"""
    return asyncio.create_task(wait_random(max_delay))
