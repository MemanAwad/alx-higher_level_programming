#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Rectangle class"""


class Rectangle(BaseGeometry):
    """ derived class"""

    def __init__(self, width, height):
        """ the init method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
