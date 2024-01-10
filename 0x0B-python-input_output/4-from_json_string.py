#!/usr/bin/python3
"""module to return object in JSON reps a string"""

import json


def from_json_string(my_str):
    """
    Args:
        my_str: string to be loaded
    Returns: json reps
    """
    return json.loads(my_str)
