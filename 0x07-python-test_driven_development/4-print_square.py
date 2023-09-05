#!/usr/bin/python3
"""
A function that prints a square with the character #
"""


def print_square(size):
    """
    prints the a square of #
    Args:
        size (int): the size lenght of the square
    """
    message = (
        "size must be an integer",
        "size must be >= 0"
    )

    if not isinstance(size, int):
        raise TypeError(message[0])
    elif size < 0:
        raise ValueError(message[0])
    else:
        for i in range(size):
            print("{}".format("#" * size))
