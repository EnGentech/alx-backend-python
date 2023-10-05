#!/usr/bin/env python3
"""
Author: Iberedem Inyang [EnGentech]
This file returns a complex data annotation
for a list dataType
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
