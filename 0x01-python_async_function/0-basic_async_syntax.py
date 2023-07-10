#!/usr/bin/env python

"""The basics of asyncio. Concurrency, Multithreading and Parallelism."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that waits for a particular amount of
    time and returns the amount of time it waited for
    """
    secs = random.uniform(0, max_delay)
    await asyncio.sleep(secs)
    return secs
