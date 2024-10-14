#!/usr/bin/env python3
"""Module: 9-element_length"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples, each containing an element and its length."""
    return [(i, len(i)) for i in lst]
