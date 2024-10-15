#!/usr/bin/env python3
"""Module: 0-basic_async_syntax"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument and
    waits for a random delay between 0 and max_delay
    :returns the random delay.
    """
    sleep_time: float = uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
