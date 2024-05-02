#!/usr/bin/env python3
"""
Zooms in on each item in a tuple by replicating each item
by a specified factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Returns a tuple containing each item in the input tuple replicated by
    the factor."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)


zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
