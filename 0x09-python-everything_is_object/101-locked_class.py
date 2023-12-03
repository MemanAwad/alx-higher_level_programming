#!/usr/bin/python3
class LockedClass(object):
    """ class that prevent making object for it
    unless its called firet_name"""
    __slots__ = 'first_name'
