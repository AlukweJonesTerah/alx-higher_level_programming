#!/usr/bin/python3
"""module to write a string to text"""


def write_file(filename="", text=""):
    """
    Args:
        filename: file to be written
        text: string to be written
    Returns: number of chars written
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
