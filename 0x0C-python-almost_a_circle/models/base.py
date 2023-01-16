#!/usr/bin/python3
"""
module that creates a base class
"""


class Base:
    """
    class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        the init method initiales the value id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
