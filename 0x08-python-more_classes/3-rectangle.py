#!/usr/bin/python3
"""Modules
"""


class Rectangle:
    """Represent 2D rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialization

        Args:
            width and height both integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrive the width of the rectangle

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Retrive the height of the rectangle

        Return:
            int: height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Update the width
        """
        self.__width = value
        try:
            if isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
        except Exception as e:
            e
        return

    @height.setter
    def height(self, value):
        """Update the width
        """
        self.__height = value
        try:
            if isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
        except Exception as x:
            x
        return

    def area(self):
        """Return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimater of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width*2 + self.__height*2

    def __str__(self):
        """Return the string  rep. of the width and height of the rectangle
        """
        if self.__width == 0 or self.height == 0:
            return ''
        else:
            result = list(map(
                lambda var: "#" * self.width + '\n' * (var != self.height - 1),
                range(self.height)
            ))
        return "".join(result)
