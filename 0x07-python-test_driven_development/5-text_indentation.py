#!/usr/bin/python3
"""
module to print a new line after '.', ':', '?'

"""
def text_indentation(text):

    if type(text) is not str:
        raise TypeError('text must be a string')

    starting = False
    new_string = ''
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
