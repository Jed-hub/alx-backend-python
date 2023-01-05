#!/usr/bin/env python3
"""
Sum list module
"""
from typing import List


def sum_list(input_list: list[float]) -> float:
    """
    Returns the sum of input list as float
    """
    f_sum: float = 0
    for num in input_list:
        f_sum += num

    return f_sum
