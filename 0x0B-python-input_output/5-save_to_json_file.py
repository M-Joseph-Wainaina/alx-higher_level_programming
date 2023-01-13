#!/usr/bin/python3
"""
save an object in a file using the json string
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json
    args:
        my_obj - object to be saved in file
        filename - path to the file to save the json string
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
