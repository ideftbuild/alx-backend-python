#!/usr/bin/env python3
"""Module: 1-async_comprehension"""
from typing import List, Callable


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension"""
    async_generator: Callable = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
