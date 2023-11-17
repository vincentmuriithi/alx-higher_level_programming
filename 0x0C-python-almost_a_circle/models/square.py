#!/usr/bin/python3

"""
Module defines a class square
tht inherits from rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        defines class variables
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloaded __str__ method for Square class.

        Returns:
            str: Formatted string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
