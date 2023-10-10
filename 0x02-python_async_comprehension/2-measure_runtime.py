#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This is an asyncio loop function
that will loop through and print a file for 10 times
"""


import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    return the time extend of asyncio
    process within the function
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
