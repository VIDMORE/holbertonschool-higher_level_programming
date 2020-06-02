#!/usr/bin/python3
"""This module defines the function lookup"""


def lookup(obj):
    """
    Function to get list of available attributes
    and methods of an object

    Return:
        list
    """

    return dir(obj)
