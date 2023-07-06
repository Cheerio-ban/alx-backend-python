#!/usr/bin/env python3
"""
Type annotated function that takes in a list of mixed type.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of a mixed type of list as float"""
    total: float = 0.00
    for elem in mxd_lst:
        total += elem
    return total
