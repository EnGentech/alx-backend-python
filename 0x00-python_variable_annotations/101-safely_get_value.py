#!/usr/bin/env python3
"""
Author: Iberedem Inyang [EnGentech]
This file returns a complex data annotation
for a multiple dataType
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''
    return a complex type annotation
    '''
    if key in dct:
        return dct[key]
    else:
        return default
