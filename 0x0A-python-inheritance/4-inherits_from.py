#!/usr/bin/python3
""" inherits from method"""


def inherits_from(obj, a_class):
    """ function to determine if the class is a subclasss"""

    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False
