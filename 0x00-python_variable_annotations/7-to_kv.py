#!/usr/bin/env python3
"""
Function to_kv that takes a string and float and converts them
to tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of parameters (k, v^2)
    """
    square: float = v ** 2
    return (k, square)
