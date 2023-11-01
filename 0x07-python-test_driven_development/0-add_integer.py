#!/usr/bin/python3

def add_integer(a, b = 98):
    """
    This is a function that adds two numbers(integers)
    >>> add_integer(7, 7)
    14
    >>> add_integer(8.5, 9.678)
    17
    >>> add_integer("string", 9)
    a must be an integer
    >>> add_integer(89, "hello")
    b must be an integer
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return int(a + b)
