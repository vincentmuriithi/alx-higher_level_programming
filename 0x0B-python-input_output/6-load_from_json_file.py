#!/usr/bin/python3

"""
Defines a function that creates an object
from json
"""

import json


def load_from_json_file(filename):

    """
    Create a Python object from a JSON file.

    Parameters:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON file.
    """

    with open(filename, "r",  encoding="utf-8") as f:
        json.load(f)
