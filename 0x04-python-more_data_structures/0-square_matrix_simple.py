#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A square matrix function

    Parameters:
         Matrix

    Return:
        The matrix
        The square of the matrix entry
    """

    return([list(map(lambda x: x * x, row) for row in matrix]))
