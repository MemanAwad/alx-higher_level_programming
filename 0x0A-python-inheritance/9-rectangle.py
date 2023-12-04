#!/usr/bin/python3
""" Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ derived class"""

    def __init__(self, width, height):
        """ the init method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """ function to compute the area"""

        return self.__width * self.__height

    def __str__(self):
        """ str function"""

        return "[Rectangle] " + str(self.__width) + " /" + str(self.__height)
