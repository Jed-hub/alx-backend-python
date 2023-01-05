#!/usr/bin/env python3
"""
First element of a sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return lst or none
    """
    if lst:
        return lst[0]
    else:
        return None
