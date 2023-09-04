#!/usr/bin/python3
"""
A function that divide all elements of a matrix
"""
def matrix_divided(matrix, div):
    outer_matrix = []
    size = len(matrix[0])
    try:
        if not isinstance(matrix, list([int, float])):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif not isinstance(div, type(int), type(float)):
           raise TypeError("div must be a number")
        elif div == 0:
           raise ZeroDivisionError("division by zero")

    for row in matrix:
        inner_list = []
        if not instance(row, type(row), list()):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, type(int), type(float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            inner_list.append(round(num / div, 2))
        outer_matrix.append(inner_list)
    return (outer_matrix)
