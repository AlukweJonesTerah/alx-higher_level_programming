#!/usr/bin/python3
"""module to append a string to text"""


def append_write(filename="", text=""):
    """
    Args:
        filename: file to be written
        text: string to be appended
    Returns: number of chars written
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
