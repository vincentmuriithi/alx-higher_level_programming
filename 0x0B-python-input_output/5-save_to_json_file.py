#!/usr/bin/python3

"""
Defines a function for saving a json object
into a file
"""

import json


def save_to_json_file(my_obj, filename):

    """
    Save the given object to a text file using JSON representation.

    Parameters:
        my_obj: Any valid JSON-serializable object.
        filename: The name of the file to which the object will be saved.
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
