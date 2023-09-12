#!/usr/bin/python3
"""Module import
"""


def class_to_json(obj):
    """Function that retrieve dictionary description
    of an object.
    """
    if "__dict__" in dir(obj):
        return obj.__dict__
