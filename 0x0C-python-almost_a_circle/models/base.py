#!/usr/bin/python3
""" base class module"""
import json
import os.path


class Base:
    """ base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ function to convert string to json"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string represintaion in a file """

        if list_objs is None:
            listt = []
        else:
            listt = [obj.to_dictionary() for obj in list_objs]

        class_name = cls.__name__
        filename = class_name + ".json"

        with open(filename, "w") as file:
            file.write(cls.to_json_string(listt))

    @staticmethod
    def from_json_string(json_string):
        """function converts string to json"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ function to load from a file"""

        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            content = cls.from_json_string(file.read())
        return [cls.create(**index) for index in content]
