#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = list(sorted(a_dictionary.items()))
    for value in new_list:
        print(*value, sep=": ")
