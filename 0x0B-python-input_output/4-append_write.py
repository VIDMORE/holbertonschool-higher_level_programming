#!/usr/bin/python3
"""This module defines the function append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at end of a text file, returns # of characters written

    Args:
        filename (str): File
        text (str): text
    """

    nb_characters = 0

    with open(filename, 'a', encoding="utf-8") as file:
        nb_characters = file.write(text)

    return nb_characters
