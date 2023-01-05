#!/usr/bin/env python3
"""
Sum mixed list module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the list as a float
    """
    f_sum: float = 0
    for num in mxd_lst:
        f_sum += num

    return f_sum
