#!/usr/bin/python3
import json

"""
module to convert a string to json representation
"""

def to_json_string(my_obj):
    """
    to_json_string - convert a string to json

    args:
        my_obj - object to converted
    """
    return json.dumps(my_obj)

