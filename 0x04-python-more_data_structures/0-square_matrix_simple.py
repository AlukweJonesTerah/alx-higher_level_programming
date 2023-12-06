#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    str(matrix)
    new_matrix = [[column ** 2 for column in row]
            for row in matrix]
    return new_matrix

