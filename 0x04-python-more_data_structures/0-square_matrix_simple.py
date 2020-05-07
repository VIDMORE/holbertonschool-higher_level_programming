#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for lists in matrix:
        new_list += [[x ** 2 for x in lists]]
    return new_list
