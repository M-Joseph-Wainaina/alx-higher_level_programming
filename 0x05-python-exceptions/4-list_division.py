#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    quo = 0
    quo_list = [None] * list_length
    while i < list_length:
        try:
            quo = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            quo = 0
        except ZeroDivisionError:
            print("division by 0")
            quo = 0
        except IndexError:
            print("out of range")
            quo = 0
        finally:
            quo_list[i] = quo
        i += 1
    return quo_list

    
