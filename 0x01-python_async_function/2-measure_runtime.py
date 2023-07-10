#!/usr/bin/env python3
"""Measuring the runtime"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Function measures the runtime"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_taken = time.perf_counter() - s
    return time_taken / n
