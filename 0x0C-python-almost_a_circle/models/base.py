#!/usr/bin/python3
"""This module defines the class Base"""

import json
from os import path
import csv


class Base:
    """
    Class that builds a Base

    Attributes::
        attr1(__nb_objects): counter of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance of the Base

        Args:
            id: id for each instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        obj_list = []

        if list_objs is None:
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
                file.write(Base.to_json_string(obj_list))
        else:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
                file.write(Base.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to an object"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        obj_list = []
        instance_list = []

        if not path.exists(cls.__name__ + ".json"):
            return obj_list
        else:
            with open(cls.__name__ + ".json", encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dic in obj_list:
                    instance_list.append(cls.create(**dic))
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""

        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            fieldnames = ['id', 'size', 'x', 'y']

        with open(cls.__name__ + ".csv", 'w', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""

        instance_list = []

        if not path.exists(cls.__name__ + ".csv"):
            return []
        else:
            with open(cls.__name__ + ".csv", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    instance_list.append(cls.create(**row))
            return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
