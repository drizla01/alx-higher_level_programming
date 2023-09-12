#!/usr/bin/python3
"""Import Module
"""


def write_file(filename="", text=""):
    with open(filename, encoding="utf-8", mode="a") as f:
        f.write(text)
