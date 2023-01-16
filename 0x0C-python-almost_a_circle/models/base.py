#!/usr/bin/python3
"""
module that creates a base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the json string rep of list_dictionary
        """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
                return "[]"
        return json.dumps(list_dictionaries)


