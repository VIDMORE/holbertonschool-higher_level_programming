#!/usr/bin/python3
def number_of_lines(filename=""):

    counter = 0

    with open(filename, 'r', encoding="utf-8") as file:
        for _ in file:
            counter += 1

    return counter
