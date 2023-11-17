#!/usr/bin/python3

"""
module to add items into python list
"""

import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Save the given object to a text file using JSON representation.

    Parameters:
        my_obj: Any valid JSON-serializable object.
        filename: The name of the file to which the object will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Parameters:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Load existing data from the file or create an empty list
try:
    existing_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_data = []

# Add command-line arguments to the list
for arg in sys.argv[1:]:
    existing_data.append(arg)

# Save the updated list to the file
save_to_json_file(existing_data, 'add_item.json')

print("Arguments added to 'add_item.json'")
