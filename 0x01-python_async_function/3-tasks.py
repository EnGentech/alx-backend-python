#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: this code defines an ordinary function
which in turn returns a type of asyncio task function
"""


import asyncio


get = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A basic function that returns asyncio_task class"""

    return asyncio.create_task(get(max_delay))
