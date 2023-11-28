#!/usr/bin/python3
""" function that will print the full name
Args:
    first_name(str): the frist name
    last_name(str): the last name"""

def say_my_name(first_name, last_name=""):
    """ function that print the full name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
