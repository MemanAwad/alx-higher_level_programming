#!/usr/bin//python3
""" ''class_to_json'' module"""


def class_to_json(obj):
    """class to json module
     Returns the dictionary description with simple data structures:
    - list
    - dictionary
    - string
    - integer
    - boolean
    """

    attr = {}
    for key in obj.__dict__:
        value = getattr(obj, key)
        if type(value) in [list, dict, str, int, bool]:
            attr[key] = value

    return attr
