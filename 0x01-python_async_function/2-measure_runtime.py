#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This is a basic python function that calls
an asyncio run function to execute a previous function
for a given specifics
"""


import asyncio
from time import time


get = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A basic time measure function"""

    begin = time()
    asyncio.run(get(n, max_delay))
    return (time() - begin) / n
