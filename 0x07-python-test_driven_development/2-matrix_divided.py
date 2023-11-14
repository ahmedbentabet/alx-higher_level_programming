#!/usr/bin/python3
"""Divide a matrix Module."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix."""

    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    for i, row in enumerate(matrix):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
