#!/usr/bin/python3
def max_integer(my_list=[]):
    new_l = []
    new_l = [True if value % 2 == 0 else False for value in my_list]
    return new_l
