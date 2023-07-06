#!/usr/bin/env python3
"""Return values, add type annotations to the function"""

from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Looking into TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
