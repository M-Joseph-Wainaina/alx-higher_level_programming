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

    def to_json(self):
        """
        public method to retrieve json rep of the class
        """
        return self.__dict__
