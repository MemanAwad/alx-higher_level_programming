#!/usr/bin/python3

""" this module is going to make a rectangle class"""


class Rectangle:
    """ this class is going to define a reactangle"""

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ the init method"""
        self.__width = height
        self.__height = width

    @property
    def width(self):
        """ return the width of the rectangle"""

        return self.__height

    @property
    def height(self):
        """ return the height of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """ to set the value of the width """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ to set the value of the height """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
