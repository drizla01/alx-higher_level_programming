#!/usr/bin/python3
"""
import modules
"""


def matrix_mul(m_a, m_b):
    """
    A function that multiply two matrix

    Args:
        m_a (int or float) - the first matrix
        m_b (int or float) - the second matrix

    Returns:
        The product of the two matrix

    Exceptions:
    """
    messages = (
        "m_a must be a list",
        "m_b must be a list",
        "m_a must be a list of lists",
        "m_b must be a list of lists",
        "m_a can't be empty",
        "m_b can't be empty",
        "m_a should contain only integers or floats",
        "m_b should contain only integers or floats",
        "each row of m_a must be of the same size",
        "each row of m_b must be of the same size",
        "m_a and m_b can't be multiplied"
    )
    if not isinstance(m_a, list):
        raise TypeError(messages[0])
    elif not isinstance(m_b, list):
        raise TypeError(messages[1])
    elif not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError(messages[2])
    elif not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError(messages[3])
    elif not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a) or not m_a:
        raise ValueError(messages[4])
    elif not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b) or not m_b:
        raise ValueError(messages[5])
    elif not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a) or not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError(messages[6])
    elif not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b) or not all(isinstance(ele, (int, float))for row in m_b for ele in row):
        raise TypeError(messages[7])
    elif (len(m_a) != len(m_a[0])):
        raise TypeError(messages[8])
    elif (len(m_b) != len(m_b[0])):
        raise TypeError(messages[9])
    elif len(m_a[0]) != len(m_b):
        raise ValueError(messages[10])
    else:
        m_mul = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
        for row_a in range(len(m_a)):
            for col_b in range(len(m_b)):
                for row_b in range(len(m_b)):
                    m_mul[row_a][col_b] += m_a[row_a][row_b] * m_b[row_b][col_b]
        return m_mul
