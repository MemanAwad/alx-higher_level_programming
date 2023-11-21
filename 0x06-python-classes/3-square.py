#!/usr/bin/python3

"""This module is going to initiate a python empty class"""


class Square:
    """ empty class Square that defines a square

    Attributes:
            size (int): hold the size of the square."""

    __size = 0

    def __init__(self, size=0):
        """ initializer of the default size of the object

        Args:
            size (str): the size of the square."""

        try:
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")

    def area(self):
        """ Function to coount the area of the square

        Returns:
            the calculated size of the area"""

        return (self.__size * self.__size)
