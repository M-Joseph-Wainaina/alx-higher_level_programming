#!/usr/bin/python3
"""
module that contains the add_integer function

"""
def add_integer(a, b=98):
    """add_integer
    args:
        a first value
        b second value
    return:
        sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
