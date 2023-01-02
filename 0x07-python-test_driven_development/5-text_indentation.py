#!/usr/bin/python3
"""
module to print a new line after '.', ':', '?'

"""
def text_indentation(text):
    """
    text_indentation 
    function that prints two new lines after '.?:'
    spaces not required after and before the printed lines
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    text_len = len(text)
    i = 0
    while i < text_len:
        if text[i] == ' ':
            i += 1
        else:
            break

    while i < text_len:
        print(text[i], end='')
        if text[i] in '.?:':
            print('\n\n', end='')
            i += 1
            while i < text_len:
                if text[i] == ' ':
                    i += 1
                else:
                    i -= 1
                    break
        i += 1
