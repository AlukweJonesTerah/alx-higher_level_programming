#!/usr/bin/python3
"""module to define class to Json function"""


def class_to_json(obj):
    """
    Args:
        obj: json obj
    Returns: dictionary reps of a data structss
    """
    return obj.__dict__
