#!/usr/bin/python3
"""Module import here
"""
import json


def to_json_string(my_obj):
    """A function that return the JSON
    representation of an object(string)

    Args:
       my_obj - object

    Return: the JSON form
    """
    j = json.dumps(my_obj)
    return j
