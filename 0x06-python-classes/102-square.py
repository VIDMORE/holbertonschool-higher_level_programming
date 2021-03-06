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
        self.__size = size

    def area(self):
        """
        Brings the area of square

        Returns:
            The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        getter function of size

        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter function of size

        Args:
            value: value for __size attribute
        """
        if type(value) is not int or type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __lt__(self, other):
        """
        Comparator function

        Args:
            other: other object

        Returns:
            True or False
        """
        return self.size ** 2 < other.size ** 2

    def __le__(self, other):
        """
        Comparator function

        Args:
            other: other object

        Returns:
            True or False
        """
        return self.size ** 2 <= other.size ** 2

    def __eq__(self, other):
        """
        Comparator function

        Args:
            other: other object

        Returns:
            True or False
        """
        return self.size ** 2 == other.size ** 2

    def __ne__(self, other):
        """
        Comparator function

        Args:
            other: other object

        Returns:
            True or False
        """
        return self.size ** 2 != other.size ** 2

    def __gt__(self, other):
        """
        Comparator function

        Args:
            other: other object

        Returns:
            True or False
        """
        return self.size ** 2 > other.size ** 2

    def __ge__(self, other):
        """
        Comparator function

        Args:
            other: other object

        Returns:
            True or False
        """
        return self.size ** 2 >= other.size ** 2
