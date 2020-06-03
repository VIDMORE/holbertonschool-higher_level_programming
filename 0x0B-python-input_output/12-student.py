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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of an object student"""

        new_dic = {}
        if type(attrs) is list and map(lambda x: type(x) is str, attrs):
            for val in attrs:
                if val in self.__dict__:
                    new_dic[val] = self.__dict__[val]
            return new_dic
        else:
            return self.__dict__
