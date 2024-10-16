#!/usr/bin/env python3
"""Module: 2-measure_runtime"""


def measure_time(n: int, max_delay: int) -> float:
    """Calculates and returns the total execution time for the
    wait_n function"""
    from asyncio import run
    from time import perf_counter
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start = perf_counter()
    run(wait_n(n, max_delay))
    end = perf_counter()

    return (end - start) / n
