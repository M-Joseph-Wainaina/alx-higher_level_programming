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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json string representation of list_objs to a file
        """

        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            list_dictionaries = []

            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

            return f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        return a list of the json string representation
        """

        if json_string is None or len(json_string) = 0:
            return []
        return json.loads(json_string)
