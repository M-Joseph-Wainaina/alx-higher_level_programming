#!/usr/bin/python3
"""
module that return a dictionary description of a class
"""


def class_to_json(obj):
    """
    function that returns the dict description of a class
    """
    return obj.__dict__
