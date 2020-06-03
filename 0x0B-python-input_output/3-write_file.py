#!/usr/bin/python3
"""This module defines the function write_file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns number of characters written

    Args:
        filename (str): File
        text (str): text to write
    """

    nb_characters = 0

    with open(filename, 'w', encoding="utf-8") as file:
        nb_characters = file.write(text)

    return nb_characters
