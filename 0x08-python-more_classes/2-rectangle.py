#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width*2 + self.__height*2
