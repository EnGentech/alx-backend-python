#!/usr/bin/env python3

import asyncio
from random import uniform


async def wait_random(max_delay = 10):
    wait_random = uniform(0, max_delay)
    await asyncio.sleep(wait_random)
    return wait_random