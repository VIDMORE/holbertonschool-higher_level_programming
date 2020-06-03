#!/usr/bin/python3
"""This module defines the function number_of_lines"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file

    Args:
        filename (str): Filename
    """
    counter = 0

    with open(filename, 'r', encoding="utf-8") as file:
        for _ in file:
            counter += 1

    return counter
