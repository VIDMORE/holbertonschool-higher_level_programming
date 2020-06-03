#!/usr/bin/python3
"""This module creates the function class_to_json"""


def class_to_json(obj):
    """
    Returns the dictionary description of object

    Args:
        obj (object): object to use

    Returns:
        dictionary
    """

    return obj.__dict__
