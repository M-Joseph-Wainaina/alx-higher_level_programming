#!/usr/bin/python3
"""
module that contains a class that defines a rectangle

"""

class Rectangle:
    """
    class that defines a rectangle
    """
    pass
    def __init__(self, width=0, height=0):
        """
        the init method initialises the private atrributes __height and __width
        args:
            height value to set to __height
            width value to be set to __width
        """
        self.check_value(width, 'width')
        self.check_value(height, 'height')
        self.__height = height
        self.__width = width
    @property
    def width(self):
        """
        getter for __width
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        setter for width
        """
        self.check_value(value, 'width')
        self.__width = value
    @property
    def height(self):
        """
        getter for the private atr __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for __height
        """
        self.check_value(value, 'height')
        self.__height = value


    def check_value(self, value, name):
        """
        check that value is integer and greater than zero
        """

        if type(value) is not int:
            message = name + ' must be an integer'
            raise TypeError(message)
        if value < 0:
            message = name + ' must be >= 0'
            raise ValueError(message)
	

    def area(self):
        """
        function that return the area of a rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        function that returns the perimeter of a rectangle
        """
        return (2 * (self.__height + self.__width))
    
    def __str__(self):
        """
        prints a rectangle using #'s
        """
        i = 1
        j = 1
        ret = ""
        while i <= self.__height:
            j = 1
            while j <= self.__width:
                ret += "#"
                j += 1
            if i == self.__height:
                break
            i += 1 
            ret += "\n"
        return ret

    def __repr__(self):
        """
        return the dimension of the rectangle in \
                order to create a new isntance of rctangle

        """
        ret = "Rectangle (" + str(self.__width) + ", " + str(self.__height) +")" 
        return ret

    def __del__(self):
        """
        prints a message when a rectangle is being deleted
        """
        print("Bye rectangle...")
