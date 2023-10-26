#!/usr/bin/python3

class Square:
    def __init__(self, size = 0):
        self.size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

   @size.setter
   def size(self, value):
       self.__size = value
       if type(value) != int:
           raise TypeError("size must be an integer")
       if self.__size < 0:
           raise ValueError("size must > 0")

    def  my_print(self):
        if self.__size == 0:
            print()
        else:
            fr i in range(self.__size):
                for k in range(self.__size):
                    print("#", end = "")
                print()

    def position(self):
        return self.__position



