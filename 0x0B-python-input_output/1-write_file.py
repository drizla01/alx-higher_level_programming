#!/usr/bin/python3
"""Import Module
"""


def write_file(filename="", text=""):
    """Write a UTF-8 encoded text to a file."""
    numb = 0
    with open(filename, encoding="utf-8", mode="w") as f:
        numb = f.write(text)
        return numb
