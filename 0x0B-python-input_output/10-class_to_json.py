#!/usr/bin/python3
"""This module creates the function class_to_json"""


import json


def class_to_json(obj):
    """
    Returns the dictionary description of object

    Args:
        obj (object): object to use

    Returns:
        dictionary
    """

    return json.loads((json.dumps(obj.__dict__)))
