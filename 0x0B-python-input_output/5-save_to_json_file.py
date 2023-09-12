#!/usr/bin/python3
"""Import Module here
"""
from json import JSONEncoder


def save_to_json_file(my_obj, filename):
    """
    Function that write an Object to a text file,
    using JSON representation

    Args:
        my_obj - the object
        filename - file containing the text

    Returns:
        text file
    """
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(JSONEncoder().encode(my_obj))
