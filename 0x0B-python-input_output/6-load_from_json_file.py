#!/usr/bin/python3
"""Module import here
"""
import json


def load_from_json_file(filename):
    """
    A function that create an Object from a "JSON file"
    """
    with open(filename) as file:
        return json.load(file)
