#!/usr/bin/python3
"""This module defines the function from_json_string"""


import json


def from_json_string(my_str):
    """
    Returns a python object

    Args:
        my_obj (str): JSON object

    Returns:
        python object
    """

    return json.loads(my_str)
