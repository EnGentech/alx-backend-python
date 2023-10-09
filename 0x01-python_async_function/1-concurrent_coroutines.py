#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This is similar to the previous code
with the addition of a loop list comprehension to
spawn the await period for a consecutive number of times
"""


import asyncio
from typing import List


get = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function defines an asyncio cooroutine"""

    wait_times = [await get(max_delay) for wait_time in range(n)]
    return sorted(wait_times)
