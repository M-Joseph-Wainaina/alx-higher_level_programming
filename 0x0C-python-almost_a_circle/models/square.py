#!/usr/bin/python3
"""
module that defines the class square a subclass of Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init method for instatation of the square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overide the str method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """
        return the size of the square instance
        """
        return self.height

    @size.setter
    def size(self, value):
        """
        setter for the value of the square
        """
        self.height(value)
        self.width(value)
