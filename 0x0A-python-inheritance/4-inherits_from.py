#!/usr/bin/python3
"""This module defines the function inherits_from"""


def inherits_from(obj, a_class):
    """
    Function to know if an object is based
    on a given inheritance class

    Return:
        True of False
    """
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
