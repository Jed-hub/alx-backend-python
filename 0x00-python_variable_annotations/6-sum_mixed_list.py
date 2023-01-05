#!/usr/bin/env python3
"""
Sum mixed list module
"""


def sum_mixed_list(mxd_lst: list) -> float:
    """
    Returns the sum of the list as a float
    """
    f_sum: float = 0
    for num in mxd_lst:
        f_sum += num

    return f_sum
