#!/usr/bin/python3
"""
Import module here
"""

from json import JSONDecoder


def from_json_string(my_str):
    """
    function that return an object (JSON)
    to string

    Args:
        my_str - the string file

    Returns: the string
    """
    return JSONDecoder().decode(my_str)
