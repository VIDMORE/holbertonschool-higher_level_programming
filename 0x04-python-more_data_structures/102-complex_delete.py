#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = list(a_dictionary.keys())
    for val in new_list:
        if value is a_dictionary[val]:
            a_dictionary.pop(val)
    return a_dictionary
