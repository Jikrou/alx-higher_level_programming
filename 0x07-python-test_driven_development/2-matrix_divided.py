#!/usr/bin/python3
"""
A module for performing division on a matrix.

"""


def matrix_divided(matrix, div):

    """ Divide all the elements in a matrix
        matrix / div
        :return: the new matrix.  """

    if not matrix:
        err_msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err_msg)

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if div is None:
        return matrix

    if isinstance(matrix, list) \
       and all(isinstance(row, list) for row in matrix) \
       and all(isinstance(el, (int, float)) for r in matrix for el in r):
        new_matrix = []
        for row in matrix:
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            else:
                if div == 0:
                    raise ZeroDivisionError("division by zero")
            new_row = [round(elements / div, 2) for elements in row]

            new_matrix.append(new_row)
        return new_matrix
    else:
        err_msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err_msg)
