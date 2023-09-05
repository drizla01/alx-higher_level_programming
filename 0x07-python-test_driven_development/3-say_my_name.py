#!/usr/bin/python3
"""
A function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    print the first and last name of a person

    Args:
        first_name  (str): the first name of the person
        last_name (str): the last name of the person

    Return:
          the first and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
