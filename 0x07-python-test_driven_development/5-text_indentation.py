#!/usr/bin/python3
"""This module defines the text_indentation function"""


def text_indentation(text):
    temp_text = ''
    """
    Function that prints a text

    Args:
        text (str): Text given by the user.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    for character in text:
        temp_text += character
        if character in ['?', '.', ':']:
            print(temp_text.strip() + "\n")
            temp_text = ''
    print(temp_text.strip(), end="")
