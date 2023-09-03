#!/usr/bin/python3
"""
A module that summ two numbers
"""


def add_integer(a, b=98):
    """
    function that add two numbers

    parameters:
    a : first parameter
    b : second paramter
    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        return (int(a + b))
    except Exception as e:
        return (e)
