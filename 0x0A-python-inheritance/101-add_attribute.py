#!/usr/bin/python3
def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible."""
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
    