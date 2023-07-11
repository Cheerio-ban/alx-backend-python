#!/usr/bin/env python3
""" measure runtime """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures runtime. """
    s1 = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    s2 = time.perf_counter()
    return s2 - s1
