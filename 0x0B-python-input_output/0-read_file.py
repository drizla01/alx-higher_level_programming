#!/usr/bin/python3
"""Import Module
"""


def read_file(filename=""):
    """
    filename: the text/binary file containing the item to be read
     using with to close the file and avoid waste of memory.
    """
    with open(filename, encoding="utf-8", mode="r") as f:
        for line in f.read():
            print(line, end="")
