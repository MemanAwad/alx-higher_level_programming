#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor"""

        super().__init__(size, size, x, y, id=None)

    @property
    def size(self):
        """return the size"""

        return self.height

    @size.setter
    def size(self, value):
        """size setter"""

        self.width = value
        self.height = value

    def __str__(self):
        """return string repreintaion of the square"""

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """to update the attributes of square object"""

        if args is not None and len(args) != 0:
            length = len(args)
            i = 0
            if i < length:
                self.id = args[0]
            i += 1
            if i < length:
                self.size = args[1]
            i += 1
            if i < length:
                self.x = args[2]
            i += 1
            if i < length:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """function that return the dictionary representaion"""

        dic = {}
        for i in ["id", "x", "size", "y"]:
            dic[i] = getattr(self, i)
        return dic
