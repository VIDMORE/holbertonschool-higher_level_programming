#!/usr/bin/python3
"""This module creates a Class Square"""


class Square:
    """Class Square with a constuctor method"""

    def __init__(self, size=0):
        """
        Initializes square

        Args:
            size: size for __size attribute
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Brings the area of square

        Returns:
            The area of the square
        """
        return self.__size * self.__size
