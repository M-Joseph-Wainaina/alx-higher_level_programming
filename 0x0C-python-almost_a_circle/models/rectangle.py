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
        self.check_args(width=width, height=height, x=x, y=y)
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
        self.check_args(width=value)
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
        self.check_args(height=value)
        self.__height = value

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
        self.check_args(x=value)
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
        self.check_args(y=value)
        self.__y = value

    def check_args(self, **kwargs):
        """
        validation for the setters and instatiation
        """
        for kwarg in kwargs:
            if type(kwargs[kwarg]) is not int:
                raise TypeError(f"{kwarg} must be an integer")
            if kwarg in ['width', 'height']:
                if kwargs[kwarg] <= 0:
                    raise ValueError(f"{kwarg} must be > 0")
            if kwarg in ['x', 'y']:
                if kwargs[kwarg] < 0:
                    raise ValueError(f"{kwarg} must be >= 0")

    def area(self):
        """
        public method that return the value of area
        """
        return self.__width * self.__height

    def display(self):
        """
        print the instance of the rectangle in the stdout using #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
        method to update the values of the instance
        """
        argsNo = len(args)
        modif_arg = ['id', 'width', 'height', 'x', 'y']
        if argsNo > 5:
            argsNo = 5

        if argsNo > 0:
            for i in range(argsNo):
                setattr(self, modif_arg[i], args[i])

        elif len(kwargs) > 0:
            for key in kwargs:
                if key in modif_arg:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """
        overide the str method
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
                self.id, self.x, self.y, self.width, self.height
                )

    def to_dictionary(self):
        """
        method return the dictionary description of the instance
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
