#!/usr/bin/python3

"""
This module contains a function that
returns the list of available
attributes and methods of an objects
"""


def lookup(obj):

    """ returns a list of possible attributes """

    return dir(obj)
