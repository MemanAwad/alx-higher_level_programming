#!/usr/bin/python3
""" class mt_int that inherits from int"""


class MyInt(int):
    """ my int class"""

    def __eq__(self, other):
        """ is equal function"""

        return type(self) == type(other)

    def __ne__(self, other):
        """ is not equal function"""

        return type(self) != type(other)
