#!/usr/bin/python3
"""Module import
"""


class Student:
    "The class of student"

    def __init__(self, first_name, last_name, age):
        """Initialization of variables with public instance attribute
        of firstname, lastname and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to retrieve a dictionary representation of a student"""
        if "__dict__" in dir(self):
            return self.__dict__
