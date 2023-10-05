#!/usr/bin/python3
"""
A  type-annotated function floor which
takes a float n as argument and returns
the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    This function takes a single argument as float,
    convert the float into math.floor and returns
    an integer data type
    """
    return math.floor(n)
