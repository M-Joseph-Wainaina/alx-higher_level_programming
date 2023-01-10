#!/usr/bin/python3
"""
module to that contains file manipulations
"""

def read_file(filename=""):
   """
   read_file - read a file and print it to stdout

   args:
        filename - path to the file to be read
    """
    with open(filename, 'r', encoding="UTF8") as f:
        read_data = f.read()
        print(read_data, end='')
