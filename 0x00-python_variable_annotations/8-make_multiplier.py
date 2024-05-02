#!/usr/bin/env python3
"""Takes a float as argument and returns a function that multiplies a float by
the input argument."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiplier_fn(val: float) -> float:
        return val * multiplier
    return multiplier_fn
