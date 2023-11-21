#!/usr/bin/python3

"""This module is going to initiate a python empty class"""


class Square:
    """ empty class Square that defines a square

    Attributes:
            size (int): hold the size of the square.
            position (int: tuble): hold the """

    __size = 0
    __position = [],

    def __init__(self, size=0, position=(0, 0)):
        """ initializer of the default size of the object
        and the deafualt values of the position

        Args:
            size (str): the size of the square.
            position(int, tuble): the position of the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ function to retrive the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """ function to set the size"""

        try:
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        except TypeError:
            print("size must be an integer")

    def area(self):
        """ Function to coount the area of the square
        Returns:
            the calculated size of the area"""

        return (self.__size * self.__size)

    def my_print(self):
        """ function to print the square"""

        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """function to retreive the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """ function to initaikize the tuble"""

        try:
            self.__position = [value, value]
        except TypeError:
            print("position must be a tuple of 2 positive integers")
