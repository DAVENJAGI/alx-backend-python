#!/usr/bin/python3

import random


async def wait_random(max_delay=10.0):
    """
    An async co-routine that awaits for random delay btwn 0 and max_delay
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time


async def main():
    """
    Awaits for random time between 0 and default wait time
    """
    delay = await wait_random(5.0)
    print(f"waited for {delay:.2f} seconds")


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
