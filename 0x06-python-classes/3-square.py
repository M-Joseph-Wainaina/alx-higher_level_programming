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
        self.__size = size
    def area(self):
        """area - function that computes the area of square

        args:
            none
        return:
            area
        """
        return self.__size * self.__size
