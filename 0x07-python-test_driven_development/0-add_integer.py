#!/usr/bin/python3
"""
add-integer module
adds 2 ints
"""


def add_integer(a, b=98):
    """
    Args:
        a: value 1
        b: value 2
    Returns: addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
