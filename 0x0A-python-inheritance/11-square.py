#!/usr/bin/python3
"""This module defines the class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that builds a rectangle"""

    def __init__(self, size):
        """
        Initializes instance of the square

        Args:
            size: size for __size attribute
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns string representation"""

        return "[Square] {}/{}".format(self.__size, self.__size)
