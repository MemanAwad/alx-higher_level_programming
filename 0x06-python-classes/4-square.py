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
        self.__size = size

    @property
    def size(self):
        """ function to retrive the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """ function to set the size"""

        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """ Function to coount the area of the square
        Returns:
            the calculated size of the area"""

        return (self.__size * self.__size)
