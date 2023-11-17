#!/usr/bin/python3

"""
module to retreve json class attributes
"""


def class_to_json(obj):
    """
    dict obj
    """
    return obj.__dict__
