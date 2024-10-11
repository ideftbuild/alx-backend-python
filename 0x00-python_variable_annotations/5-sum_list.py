#!/usr/bin/env python3
"""
Module: 5-sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate and return the sum of elements in a list of floats."""
    from functools import reduce
    return reduce(lambda x, y: x + y, input_list)
