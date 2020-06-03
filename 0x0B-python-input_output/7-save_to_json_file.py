#!/usr/bin/python3
"""This module defines the function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using JSON

    Args:
        my_obj (str): object to use
        filename (str): file
    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
