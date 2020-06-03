#!/usr/bin/python3
"""This module defines the function load_from_json_file"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename (str): JSON file to create an Object from

    Returns:
        python object
    """

    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
