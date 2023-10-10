#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: This is an asyncio loop function
that will loop through and print a file for 10 times
"""


import asyncio


get = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """comprehension loop through a data using asyncio module"""
    return [_ async for _ in get()]
