#!/usr/bin/python3
""" square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ the square class"""

    def __init__(self, size):
        """constructor"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ str magic function"""

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
