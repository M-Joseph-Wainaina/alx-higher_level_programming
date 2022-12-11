#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        a = ord(str[i])
        if a >= 97 and a <= 122:
            a = a - 32
        print("{}".format(chr(a)), end='')
    print()

        
