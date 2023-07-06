#!/usr/bin/env python3
"""
Typed function that returns a function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Complex function - returns a function"""
    def multiply(value: float) -> float:
        """Multiplies two floats"""
        return value * multiplier
    return multiply
