#!/usr/bin/python3
"""Module import here
"""
from json import JSONDecoder


def load_from_json_file(filename):
    """
    A function that create an Object from a "JSON file"
    """
    lines = []
    with open(filename, encoding="utf-8", mode="w") as file:
        for line in file.readlines():
            lines.append(line)

    return JSONDecoder().decode("".join(lines))
