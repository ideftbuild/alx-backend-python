#!/usr/bin/env python3
"""Module: 4-tasks"""
from typing import Callable, List
from asyncio import as_completed


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random n times with the specified delay
    :returns a list of the delays in ascending order"""
    delays: List[float] = []
    task_wait_random = __import__('3-tasks').task_wait_random

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
