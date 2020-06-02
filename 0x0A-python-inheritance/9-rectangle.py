#!/usr/bin/python3
"""This module defines the class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that builds a Rectangle"""

    def __init__(self, width, height):
        """
        Initializes instance of the rectangle

        Args:
            width: width for __width attribute
            height: height for __height attribute
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of instance"""

        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
