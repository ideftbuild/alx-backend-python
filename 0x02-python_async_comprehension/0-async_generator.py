#!/usr/bin/env python3
"""Module: 0-async_generator"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async generator that yields random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
