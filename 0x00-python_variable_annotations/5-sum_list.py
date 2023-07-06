#!/usr/bin/env python3
"""
Module contains a type annotated function that adds all flost in a list
and returns it as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums all floats in a list"""
    total: float = 0.00
    for elem in input_list:
        total += elem
    return total
