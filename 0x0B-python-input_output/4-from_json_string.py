#!/usr/bin/python3
"""
module to return a a python object from a json string
"""
from json import loads


def from_json_string(my_str):
    """
    from_json_string to python object
    args:
        json string
    return:
        pyobject
    """
    return loads(my_str)
