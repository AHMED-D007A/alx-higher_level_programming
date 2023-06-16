#!/usr/bin/python3
"""
this is a divide module for dividing matrix.

this module supplies only one function matrix_divided().
it is a function that divide every element in the matrix.
"""


def matrix_divided(matrix, div):
    """this is a function for dividing a matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(element) > 0 for element in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(element) == len(matrix[0]) for element in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for element in matrix:
        if not isinstance(element, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not all(isinstance(x, (int, float)) for x in element):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for element in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), element)))

    return new_matrix
