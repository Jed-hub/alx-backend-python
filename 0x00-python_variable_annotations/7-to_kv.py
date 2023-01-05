#!/usr/bin/env python3
"""
String and in/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple
    """
    concat: Tuple(str, Union[int, float]) = (k, v**2)

    return concat
