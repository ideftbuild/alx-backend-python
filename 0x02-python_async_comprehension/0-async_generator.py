#!/usr/bin/env python3
"""Module: 0-async_generator"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that yields random numbers between 0 and 10
    after a second delay for a total of 10 iterations
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
