#!/usr/bin/python3
"""
module that creates a class rectangle which inherits from base class
"""
from models.base import Base


class Rectangle(Base):
    """
    class rectangle defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        the init method to initialise the rectangle attributes
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter method to get the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for the width private attribute
        """
        self.__width = value

    @property
    def height(self):
        """
        getter method for height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        getter method for height
        """
        self.__height = height

    @property
    def x(self):
        """
        getter method for x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for height
        """
        self.__x = value

    @property
    def y(self):
        """
        getter method for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y
        """
        self.__y = value
