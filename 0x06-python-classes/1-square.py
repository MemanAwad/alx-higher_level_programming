#!/usr/bin/python3

"""This module is going to initiate a python empty class"""


class Square:
    """ empty class Square that defines a square """

    __size = None

    def __init__(self, size=None):
        """ initializer of the default size of the object"""

        self.__size = size

