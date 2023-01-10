#!/usr/bin/python3
"""
module to that contains file manipulations
"""


def read_file(filename=""):
    """
    read_file - readfile and print it to the stdout

    args:
        filename - path to the file to be read
    """

    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end='')
