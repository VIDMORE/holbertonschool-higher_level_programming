#!/usr/bin/python3
"""This module defines the class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """Class that builds a Rectangle"""

    def __init__(self, width, height):
        """
        Initializes instance of the rectangle

        Args:
            width: width for __width attribute
            height: height for __height attribute
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
