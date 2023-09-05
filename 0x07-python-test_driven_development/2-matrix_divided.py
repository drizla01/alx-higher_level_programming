#!/usr/bin/python3
"""
A function that divide all elements of a matrix
"""
def matrix_divided(matrix, div):
    """ divide all elements of a matrix

    Args:
        matrix: a list of list containing integers or floats
        div: the number use as a divisor

    Return:
        list: a new matrix containing the result after using div
    """
    result = []
    size = [0, 0]
    message = (
        "matrix must be a matrix (list of lists) of integers/floats",
        "Each row of the matrix must have the same size",
        "div must be a number",
        "division by zero"
    )

    if not isinstance(matrix, list):
        raise TypeError(message[0])
    size[0] = len(matrix)
    if size[0] == 0:
        raise TypeError(message[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message[0])
        elif len(row) == 0:
            raise TypeError(message[0])
        else:
            if size[1] == 0:
                size[1] == len(row)
            elif len(row) != size[1]:
                raise TypeError(message[1])
            for col in row:
                if not isinstance(col, (int, float)):
                    raise TypeError(message[0])
    if not isinstance(div, (int, float)):
        raise TypeError(message[2])
    elif div == 0:
        raise ZeroDivisionError(message[3])
    else:
        for row in matrix:
            res_row = list(map(lambda x: round(x / div, 2), row))
            result.append(res_row)
        return (result)
