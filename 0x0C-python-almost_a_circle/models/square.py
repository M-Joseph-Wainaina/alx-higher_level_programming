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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        class that defines an update for the square instance
        """
        argsLen = len(args)
        kwargsLen = len(kwargs)
        modif_atr = ['id', 'size', 'x', 'y']

        if argsLen > 4:
            argsLen = 4

        if argsLen > 0:
            for i in range(argsLen):
                setattr(self, modif_atr[i], args[i])

        elif kwargsLen > 0:
            for kwarg in kwargs:
                if kwarg in modif_atr:
                    setattr(self, kwarg, kwargs[kwarg])

    def to_dictionary(self):
        """
        return the dictionaty description of a square instace
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
