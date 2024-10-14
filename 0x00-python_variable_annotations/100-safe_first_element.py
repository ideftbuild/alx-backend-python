#!/usr/bin/env python3
"""Module: 100-safe_first_element"""
from types import NoneType
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Returns the first element of a sequence otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
