#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This is an asyncio loop function
that will loop through and print a file for 10 times
"""


import asyncio
from random import uniform
from typing import List


async def async_generator() -> List[float]:
    """An asyncio function that
    prints a loop of random numbers"""
    for _ in range(10):
        number = uniform(0, 10)
        yield number
        await asyncio.sleep(1)
