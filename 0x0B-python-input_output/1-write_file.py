#!/usr/bin/python3
"""
module to write content into a file
"""


def write_file(filename="", text=""):
    """
    write_file - open a file or create if the file doesnt exist \
            write onto the file
    args:
        filename - path to the file
        text -  content to be added on the file
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
