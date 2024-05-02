#!/usr/bin/env python3
"""
Zooms in on each item in a tuple by replicating each item
by a specified factor.
"""
from typing import Tuple, Any, Union


def zoom_array(lst: Tuple[Any, ...], factor: Union[int, float] = 2) -> \
        Tuple[Any, ...]:
    """ Returns a tuple containing each item in the input tuple replicated by
    the factor."""
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(int(factor))
    )
    return zoomed_in


array = (12, 72, 91)


zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
