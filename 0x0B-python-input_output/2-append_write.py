#!/usr/bin/python3
"""For module importing
"""

n = 0


def append_write(filename="", text=""):
    """
    A function that append string at the end of a text file
    (UTF-8) and return the number of characters added.
    Args:
        filename - name of the file that contains the text
        text - the strings in the file
    """
    with open(filename, encoding="utf-8", mode="a") as file:
        n = file.write(text)
    return n
