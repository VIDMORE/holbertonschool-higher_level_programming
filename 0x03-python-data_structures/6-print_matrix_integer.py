#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for value in matrix:
        i = 0
        for val in value:
            if i == len(value) - 1:
                print ("{:d}".format(val), end="")
            else:
                print ("{:d} ".format(val), end="")
            i += 1
        print()
