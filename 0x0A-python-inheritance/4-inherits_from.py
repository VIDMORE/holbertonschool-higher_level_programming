#!/usr/bin/python3
"""This module defines the function inherits_from"""


def inherits_from(obj, a_class):
    """
    Function to know if an object is based
    on a given inheritance class

    Return:
        True of False
    """
    return type(obj) is not a_class
