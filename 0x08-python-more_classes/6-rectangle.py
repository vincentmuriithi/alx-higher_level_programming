#!/usr/bin/python3

"""
This is module 3 of the rectangle classs in the alx project
done by Eng vincent
"""


class Rectangle:
    """
    This class Rectangle contains properties that define a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Returns a string representation of the Rectangle using '#'.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(
                    ["#" * self.__width for _ in range(self.__height)]
                    )

    @classmethod        
    def __del__(cls):
        print("Bye Rectangle...")
        Rectangle.number_of_instances -= 1
