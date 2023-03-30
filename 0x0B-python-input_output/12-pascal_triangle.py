#!/usr/bin/python3
"""
module that prints the pascal triangle
"""


def pascal_triangle(n):
    """
    function that prints the pascals triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    i = 0
    j = 0
    temp = [1, 1]
    while i < n:
        triangle = temp[:]
        while j < len(temp) + 1:
            triangle[j] 
    
