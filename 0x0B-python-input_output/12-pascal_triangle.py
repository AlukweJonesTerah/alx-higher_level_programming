#!/usr/bin/python3
"""returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Args:
        n: ints
    Returns:an empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        if triangle:
            # For rows other than the first, calculate the elements
            # based on the previous row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
