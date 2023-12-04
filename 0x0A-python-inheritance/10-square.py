#!/usr/bin/python3
""" square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ the square class"""

    def __init__(self, size):
        """constructor"""

        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ compute the area of the square"""

        return super().area()
