#!/usr/bin/python3
"""Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constroctor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""

        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """get the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""

        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """get x"""

        return self.__x

    @x.setter
    def x(self, value):
        """set x"""

        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """get y"""

        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value):
        """ validate type and value of input"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "height" or name == "width") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "y" or name == "x") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """calculate the area"""

        return self.__width * self.__height

    def display(self):
        """display the rectangle"""

        for k in range(self.y):
            print()
        for i in range(self.__height):
            for z in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str represintation od rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update attributes values"""

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
                setattr(self, key, value)

    def to_dictionary(self):
        """function that return the dictionary representaion"""

        dic = {}
        for i in ["x", "y", "id", "height", "width"]:
            dic[i] = getattr(self, i)
        return dic
