#!/usr/bin/python3
"""This module defines the class MyList"""


class MyList(list):
    """Class that builds a MyList"""

    def print_sorted(self):
        """Prints instance"""

        print(sorted(self))
