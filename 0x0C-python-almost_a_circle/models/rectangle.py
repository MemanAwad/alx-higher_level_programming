#!/usr/bin/python3
"""Base class"""
from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "height" or name == "width" and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name == "y" or name == "x" and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return self.__width * self.__height

    def display(self):
        for k in range(self.y):
            print()
        for i in range(self.__height):
            for z in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,\
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            length = len(args)
            i = 0
            if i < length:
                self.id = args[0]
            i += 1
            if i < length:
                self.__width = args[1]
            i += 1
            if i < length:
                self.__height = args[2]
            i += 1
            if i < length:
                self.__x = args[3]
            i += 1
            if i < length:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
