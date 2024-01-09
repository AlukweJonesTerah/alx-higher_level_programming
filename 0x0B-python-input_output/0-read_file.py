#!/usr/bin/python3
""" Module that reads a file to stout"""


def read_file(filename=""):
    """
    Args:
        filename: file to be written to
    Returns: results to stdout
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read(), end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
