#!/usr/bin/python3
"""module to writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: object to be written
        filename: file to be written
    Returns: writes an Object to a text file, using a JSON representation:
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
