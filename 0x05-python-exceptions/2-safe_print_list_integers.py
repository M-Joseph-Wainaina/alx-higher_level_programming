#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    noInt = 0
    while idx < x:
        try:
            for i in (idx, my_list):
                print("{:d}".format(my_list[idx]), end='')
                idx += 1
                noInt += 1
        except (ValueError, TypeError):
            idx += 1
            pass
    print()
    return noInt

