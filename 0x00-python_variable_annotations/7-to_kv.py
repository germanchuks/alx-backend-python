#!/usr/bin/env python3
"""Takes a string and an int or float as arguments and returns a tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple. The first element is string `k`. The second element is
    the square of the int/float `v`."""
    return (k, v**2)
