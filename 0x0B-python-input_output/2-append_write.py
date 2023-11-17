#!/usr/bin/python3

"""
defines a function that appends a string to a file
"""


def append_write(filename="", text=""):

    """
    append write
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)

    return len(text)
