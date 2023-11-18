#!/usr/bin/python3

"""Defines a class Base"""

import turtle


class Base:
    """Class that defines properties of Base.

     Attributes:
        id (int): Identity of each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """
        Class method to create an instance
        with attributes set from a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Instance: Instance of the class with attributes set.
        """
        # Create a dummy instance with mandatory attributes
        dummy_instance = cls(1)

        # Use the update method to assign real values from the dictionary
        dummy_instance.update(**dictionary)

        # Return the instance with attributes set
        return dummy_instance

    @staticmethod
    def from_json_string(json_string):
        """
        Static method to convert a JSON string to a list.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method to return the
        JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Static method to open a window and draw all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        turtle.speed(1)
        turtle.pensize(2)

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.exitonclick()
