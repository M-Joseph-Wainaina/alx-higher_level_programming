#!/usr/bin/python3
"""module to store class square"""
class Square:
    """class to store the properties and methods of a square"""
    def __init__(self, size=0):
        """__init

        The init method initialises the value size

        raises TypeError if size is not int
        raises ValueError is size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area - function that computes the area of square

        args:
            none
        return:
            area
        """
        return self.__size ** 2
    def my_print(self):
        """function that prints a square

        args:
            void
        return:
            void
        """
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()

def print_square(size):
    sq = Square(size)
    sq.my_print()
