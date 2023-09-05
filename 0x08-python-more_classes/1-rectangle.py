#!/usr/bin/python3
"""
A module for working with the rectangle
"""


class Rectangle:
    """
    define a 2D rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize rectangle with width and height
        Args:
            width: with of the rectangle
            height: height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle
        Return:
            int: width of the rectangle 
        """
        return self.__width        

    @property
    def height(self):
        """
        Retrieve the height of the rectangle
        Return:
            int: height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Update width of the rectangle
        Args:
            value: int for the width
       """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Update the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
