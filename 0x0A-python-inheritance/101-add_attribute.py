#!/usr/bin/python3
"""This function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.
    Args:
        obj: object to add an attr to
        name: name of the attr to add to obj
        value: value of attr
    Returns: TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
