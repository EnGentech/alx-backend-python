#!/usr/bin/env python3
"""
Author: Iberedem Inyang [EnGentech]
This file returns a complex data annotation
for a list dataType
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    This function takes a list of floats and
    returns a float dataType
    """
    return sum(mxd_lst)
