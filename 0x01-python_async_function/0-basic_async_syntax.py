#!/usr/bin/env python3
"""Module: 0-basic_async_syntax"""

import asyncio
from random import uniform


async def wait_random(max_delay: int=10) -> float:
    sleep_time: float = uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
