#!/usr/bin/python3

"""
This module contains the matrix python code
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns a new matrix.

    Args:
        matrix (list): A list of lists of integers or floats representing the matrix.
        div (int or float): The number used as a divisor for the matrix.

    Returns:
        list: A new matrix with all elements divided by the divisor and rounded to 2 decimal places.

    Raises:
        TypeError: If the input matrix is not a valid matrix or if the divisor is not a number.
        ZeroDivisionError: If the divisor is equal to 0.
    """

    # Checking if the matrix is valid
    if not all(isinstance(row, list) for row in matrix) or not all(
        all(isinstance(num, (int, float)) for num in row) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Checking if all rows in the matrix have the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Checking if the divisor is a number and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing each element of the matrix by the divisor and rounding to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
