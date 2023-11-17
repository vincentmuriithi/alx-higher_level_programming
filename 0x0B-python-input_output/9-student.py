#!/usr/bin/python3

"""
Module defining a class
"""


class Student:
    """
    A student class
    """

    def __init__(self, first_name, last_name, age):
        """
        defines the variables for instatiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        defines json object
        """
        return (self.__dict__)
