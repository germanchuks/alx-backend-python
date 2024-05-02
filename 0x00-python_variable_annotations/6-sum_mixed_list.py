#!/usr/bin/env python3
"""Takes a list of integers and floats and returns their sum."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and float."""
    return sum(mxd_lst)
