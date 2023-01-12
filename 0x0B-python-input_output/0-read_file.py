#!/usr/bin/python3
"""
module to read a file and print it to the stdout
"""


def read_file(filename=""):
"""
read_file 
args:
    path to file to be read
"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
