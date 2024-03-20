#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [list(map(lambda x: x**2, row)) for row in matrix]
    return new_mat
