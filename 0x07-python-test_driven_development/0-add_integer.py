#!/usr/bin/python3
"""This module defines the add integer function"""


def add_integer(a, b=98):
    """
    Function that adds two integers

    Args:
        a (int): First number.
        b (int): Second number.
    Returns:
        int: Sum of the values a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
