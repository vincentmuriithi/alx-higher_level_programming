#!/usr/bin/python3

"""Defines a class Base"""

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
        Class method to create an instance with attributes set from a dictionary.

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
