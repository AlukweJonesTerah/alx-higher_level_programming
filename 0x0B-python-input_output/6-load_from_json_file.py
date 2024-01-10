#!/usr/bin/python3
"""module to writes an Object to a text file, using a JSON representation"""

import json


def load_from_json_file(filename):
    """
    Args:
        filename: file to be written from
    Returns:  creates an Object from a “JSON file”
    """
    with open(filename) as f:
        return json.load(f)
