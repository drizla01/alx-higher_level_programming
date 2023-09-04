#!/usr/bin//python3
"""
A function that divide all elements of a matrix
"""
def matrix_divided(matrix, div):
    try:
        if not isinstance(matrix, list([int, float])):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif not isinstance(div, type(int), type(float)):
           raise TypeError("div must be a number")
       elif div == 0:
           raise ZeroDivisionError("division by zero")
    outer_matrix = []
    size = len(matrix[0])

    for row in matrix:
        inner_list = []
        if not instance(row, type(row), list()):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return (round(matrix/div, 2))
