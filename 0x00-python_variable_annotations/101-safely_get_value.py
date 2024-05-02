#!/usr/bin/env python3
"""Gets and returns the value of the provided key from the dictionary if it
exists, otherwise returns the default value."""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
        -> Union[Any, T]:
    """Returns the value of the provided key from the dictionary if it exists,
    otherwise returns the default value."""
    if key in dct:
        return dct[key]
    else:
        return default
