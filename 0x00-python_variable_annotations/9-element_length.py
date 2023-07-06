#!/usr/bin/env python3
"""
Adding appropriate types to function provided.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list"""
    return [(i, len(i)) for i in lst]
