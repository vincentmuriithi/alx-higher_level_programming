#!/usr/bin/python3

"""
"""


class Student:
    """
    """
    def __init__(self, first_name, last_name, age):
        """
        derfines the variables for instatiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        defines json object
        """
        return (self.__dict__)
