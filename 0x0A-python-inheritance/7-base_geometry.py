#!/usr/bin/python3
""" BaseGeometry class"""


class BaseGeometry:
    """ Base class"""

    def area(self):
        """ method to raise an exeption"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function to validate value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
