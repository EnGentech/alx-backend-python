#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This is an asyncio loop function
that will loop through and print a file for 10 times
"""


import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An asyncio function that
    prints a loop of random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
