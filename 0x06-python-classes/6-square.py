#!/usr/bin/python3
"""module to store class square"""
class Square:
    """class to store the properties and methods of a square"""
    def __init__(self, size=0, position=(0,0)):
        """__init

        The init method initialises the value size

        raises TypeError if size is not int
        raises ValueError is size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if self.__check_tuple(position) is False \
                or self.__check_indexes(position) is False \
                or self.__check_integers(position) is False \
                or self.__check_values(position) is False :
                    raise TypeError('position must be a tuple of two positive integers')

        self.size = size
        self.position = position

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
        if self.__size == 0:
            print()

            return None
        if self.__postion[1] > 0:
            for i in range(self.__position[1]):
                print('')
        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print() 
    @property
    def property(self):
        return self.__position
    @position.setter
    def position(self, position):
        if self.__check_tuple(position) is False \
                or self.__check_indexes(position) is False \
                or self.__check_integers(position) is False \
                or self.__check_values(position) is False:

                raise TypeError('position must a tuple of two positive integers')
        self.__position = position

    def __check_tuple(self, position):
        if type(position) is tuple:
            return True
        return False

    def __check_indexes(self, position):
        if len(position) == 2:
            return True
        return False

    def __check_integers(self, position):
        if type(postion[0]) is int and type(position[1]) is int:
            return True
        return False
    def __check_values(self, postion):
        if position[0] >= 0 and position[1] >= 0:
            return True
        return False

