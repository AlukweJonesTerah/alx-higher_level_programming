#!/usr/bin/python3
"""a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: class to match the type of obj to
    Returns: true\false
    """
    if isinstance(obj, a_class):
        return True
    return False
