#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for key in a_dictionary:
        new_dic[key] = lambda value: a_dictionary[key] * 2
    return new_dic
