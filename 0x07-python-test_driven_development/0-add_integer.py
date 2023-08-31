#!/usr/bin/python3
def add_integer(a, b=98):
    if a is not (int or float):
        TypeError("a must be integer")
    if b is not (int or float):
        TypeError("b must be integer")
    return (int(a) + int(b))
