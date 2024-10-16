#!/usr/bin/env python3
"""Module: 3-tasks"""
import asyncio
from asyncio import Task
from typing import Callable


def task_wait_random(max_delay: int) -> Task:
    """Returns a asyncio.Task object that waits
    for a random delay"""
    wait_random: Callable = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
