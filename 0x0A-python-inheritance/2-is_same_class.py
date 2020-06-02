#!/usr/bin/python3
"""This module defines the function is_same_class"""


def is_same_class(obj, a_class):
    """
    Function to know if an object has the same
    type of a given class

    Return:
        True of False
    """

    return type(obj) is a_class
