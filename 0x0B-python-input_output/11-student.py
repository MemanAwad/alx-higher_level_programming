#!/usr/bin/python3
""" student class module"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """

        if attrs is None:
            return self.__dict__

        stu = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                stu[key] = value

        return stu

    def reload_from_json(self, json):
        """ relod from json function"""

        for key, value in json.items():
            setattr(self, key, value)
