#!/usr/bin/python3
"""This module was created with a bytecode"""
import math


class MagicClass:
    """Class MagicClass with a constuctor method"""
    def __init__(self, radius=0):
        """
        Initializes MagicClass

        Args:
            radius: radius for __radius attribute
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Brings the area of the circle

        Returns:
            The area of the circle
        """
        return((self.__radius ** 2) * math.pi)

    def circumference(self):
        return ((2 * math.pi) * self.__radius)
