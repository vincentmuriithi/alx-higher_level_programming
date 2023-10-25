#!/usr/bin/python3

class Square:
    def __init__(self, size = 0):
        self.size = size

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size**2

    @size.setter
    def size(self, value):
        self.__size = value

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size  must be >= 0")
