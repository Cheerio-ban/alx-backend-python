#!/usr/bin/env python3

"""Let's execute multiple coroutines at the same time with async"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int):
    """Multiple coroutines at the same time"""
    float_list: List[float] = []
    for _ in range(n):
        item: float = await wait_random(max_delay)
        float_list.append(item)
    return sorted(float_list)
