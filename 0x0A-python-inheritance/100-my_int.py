#!/usr/bin/python3
"""This module defines the class MyList"""


class MyInt(int):
    """Class that builds a MyInt"""

    def __eq__(self, o_cls):
        return bool.__ne__(self, o_cls)

    def __ne__(self, o_cls):
        return bool.__eq__(self, o_cls)
