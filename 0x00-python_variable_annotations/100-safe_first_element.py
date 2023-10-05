#!/usr/bin/env python3
"""
Author: Iberedem Inyang [EnGentech]
This file returns a complex data annotation
for a multiple dataType
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    if the element exist return something.
    '''
    if lst:
        return lst[0]
    else:
        return None
