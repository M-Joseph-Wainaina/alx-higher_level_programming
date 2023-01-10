#!/usr/bin/python3
import json
"""
module to convert to a json string to an object
"""
def from_json_string(my_str):
    """
    from_json_string - convert a json string into an object
    args:
        my_string - string to be converted
    """
    return json.loads(my_str)
