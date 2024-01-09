#!/usr/bin/python3
"""a class checking function."""
def is_same_class(obj, a_class):
    """
    Args:
        obj: object
        a_class:  class to match the type of obj to
    Returns: True or false
    """
    if type(obj) != a_class:
        return False
    return True
