#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for value in matrix:
        val = " ".join("{:d}".format(val) for val in value)
        print(val)
