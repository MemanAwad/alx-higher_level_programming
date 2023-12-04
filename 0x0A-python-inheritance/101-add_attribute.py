#!/usr/bin/python3

def add_attribute(obj, name, value):
    """ add attribute to object method"""

    try:
        setattr(obj, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
