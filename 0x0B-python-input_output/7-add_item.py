#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""
import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Create the file if it doesn't exist
open("add_item.json", "a").close()

try:
    # Load existing data from the file
    my_list = load_from_json_file("add_item.json")
except json.JSONDecodeError:
    # If the file is empty or not valid JSON, initialize with an empty list
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, "add_item.json")
