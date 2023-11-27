#!/usr/bin/python3

""" this module is going to make a rectangle class"""


class Rectangle:
    """ this class is going to define a reactangle"""

    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ the init method"""
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    def __del__(self):
        """ it will delete the instance of the class"""

        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """ return string of a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            strr = ""
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    strr += str(self.print_symbol)
                if (i < self.__height - 1):
                    strr += "\n"
            return strr

    def __repr__(self):
        """ return string representaiont of a rectangle
        that can be able to recreate a new instance"""
        strr = "Rectangle(" + str(self.__width) + ", "
        strr += str(self.__height) + ")"
        return strr

    @property
    def height(self):
        """ return the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """ to set the value of the height """

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ return the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """ to set the value of the width """

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Return the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """ returns rectangle primeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def bigger_or_equal(rect_1, rect_2):
        """ funtion that compare betwwen 2 rectangle """

        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
