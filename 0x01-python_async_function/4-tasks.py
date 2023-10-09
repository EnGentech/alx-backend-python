#!/usr/bin/env python3
"""
Author: Iberedem Inyang
Description: this code captures an import from
a given file and duplicates its function, use the
duplicated function to process anothe code
"""


import asyncio
from typing import List


get = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the function optained in get()"""
    return get(n, max_delay)
