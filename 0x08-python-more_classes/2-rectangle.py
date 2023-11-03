#!/usr/bin/python3

"""
This module contains a class Rectangle which could be imported into other
modules to perform rectangle functions
"""


class Rectangle:
    """
    This class rectangle defines various functions of a
    rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the value of the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        retrieves the value of the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        calculates the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        retrieves the current perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
