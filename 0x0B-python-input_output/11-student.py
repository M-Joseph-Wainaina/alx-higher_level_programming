#!/usr/bin/python3
"""
module that creates a class student
"""


class Student:
    """
    class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        public method to retrieve json rep of the class
        """
        ret = self.__dict__.copy()
        if self.check_attr(attr):
            for a in self.__dict__:
                if a in attr:
                    continue
                else:
                    ret.pop(a)

        return ret

    def check_attr(self, attr=None):
        """
        check that attr is a list of strings
        """
        if type(attr) == list:
            for a in attr:
                if type(a) != str:
                    return False
            return True
        return False

    def reload_from_json(self, json):
        """
        reload_from_json
        sets student attributes from a json string
        """
        for key in json:
            if key in self.__dict__.keys():
                self.__dict__[key] = json[key]
