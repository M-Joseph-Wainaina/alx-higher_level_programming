#!/usr/bin/python3
"""
module to import a pyobject from a json file
"""
import json


def load_from_json_file(filename):
    """
    func to load from a json file to a python object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
