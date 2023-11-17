#!/usr/bin/python3

"""
adds all arguments to a Python list
"""


import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Create the file if it doesn't exist
open("add_item.json", "a").close()

try:
    i = load_from_json_file("add_item.json")
except json.JSONDecodeError:
    i = []

# Append command-line arguments to the list
save_to_json_file(i + sys.argv[1:], "add_item.json")
