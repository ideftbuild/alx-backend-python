#!/usr/bin/env python3
"""Module: 1-concurrent_coroutines"""
import asyncio
from typing import Callable, List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random n times with the specified delay
    :returns a list of the delays in ascending order"""
    wait_random: Callable = __import__('0-basic_async_syntax').wait_random
    delays: List[float] = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
