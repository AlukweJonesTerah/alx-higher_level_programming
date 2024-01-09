#!/usr/bin/python3
"""module to return JSON reps a string to text"""

import json
def to_json_string(my_obj):
    """
    Args:
        my_obj: object to be decoded
    Returns: json reps
    """
    return json.dumps(my_obj)
