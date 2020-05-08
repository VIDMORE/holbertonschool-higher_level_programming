#!/usr/bin/python3
def weight_average(my_list=[]):
    su = 0
    di = 0
    if my_list:
        for values in my_list:
            su += values[0] * values[1]
            di += values[1]
    return su / di
