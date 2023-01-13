#!/usr/bin/python3
"""
module to convert an object into a json string
"""
from json import dumps


def to_json_string(my_obj):
    """
    to convert a py object into a json string
    """
    return dumps(my_obj)
