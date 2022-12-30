#!/usr/bin/python3
"""
module that contains the function say_my_name

"""

def say_my_name(first_name, last_name=''):
    """
    prints My name is <first name> <last name>
    
    args:
        first_name
        last_name - default is ''
    return:
        None
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
