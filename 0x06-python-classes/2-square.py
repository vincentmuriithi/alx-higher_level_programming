#!/usr/bin/python3

class Square:
    def __init__(self, size = 0):
        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
