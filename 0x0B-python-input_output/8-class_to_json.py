#!/usr/bin//python3
""" json class module"""


def class_to_json(obj):
    """class to json module"""

    attr = {}
    for key in obj.__dict__:
        value = getattr(obj, key)
        if type(value) in [list, dict, str, int, bool]:
            attr[key] = value

    return attr
