#!/usr/bin/python3
"""This modle creates the class Student"""


class Student:
    """
    A class named Student

    """

    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of an object student"""

        return self.__dict__
