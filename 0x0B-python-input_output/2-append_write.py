#!/usr/bin/python3
"""
module to open and write a file in append mode
"""


def append_write(filename="", text=""):
    """
    append write - open and write a file in append

    args:
        filename - path to the file
        text - text to be appended

    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
