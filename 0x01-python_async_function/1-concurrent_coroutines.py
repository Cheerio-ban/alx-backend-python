#!/usr/bin/env python3

"""Let's execute multiple coroutines at the same time with async"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Multiple coroutines at the same time"""
    fl_list = []
    for res in asyncio.as_completed([*(wait_random(max_delay)
                                    for _ in range(n))]):
        compl = await res
        fl_list.append(compl)
    return fl_list
