#!/usr/bin/python3
"""This module defines the function read_lines"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file (UTF8) and prints it to stdout

    Args:
        filename (str): Filename
        nb_lines (int): number of lines
    """
    counter = 0

    with open(filename, 'r', encoding="utf-8") as file:
        for _ in file:
            counter += 1

    with open(filename, 'r', encoding="utf-8") as file:
        if nb_lines <= 0 or nb_lines >= counter:
            for line in file:
                print(line, end='')
        else:
            for _ in range(nb_lines):
                print(file.readline(), end="")
