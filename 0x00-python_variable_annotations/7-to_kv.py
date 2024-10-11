#!/usr/bin/env python3
"""
Module: 7-to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of an
    integer or float value.
    """
    return k, (v ** 2)
