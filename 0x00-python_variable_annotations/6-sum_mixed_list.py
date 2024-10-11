#!/usr/bin/env python3
"""
Module: 6-sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate and return the sum of elements in a list of
    integers and/or floats.
    """
    from functools import reduce
    return reduce(lambda x, y: x + y, mxd_lst)
