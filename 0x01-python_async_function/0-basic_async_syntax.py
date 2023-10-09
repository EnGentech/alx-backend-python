#!/usr/bin/env python3
"""
This file creates an asynchronous content that
returns a random await time for the asyncio module
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """An asyncio function to return a random
    delay second before a value is printed"""

    wait_random = uniform(0, max_delay)
    await asyncio.sleep(wait_random)
    return wait_random
