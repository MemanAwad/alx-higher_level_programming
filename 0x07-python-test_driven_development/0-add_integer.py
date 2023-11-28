#!/usr/bin/python3

""" this function is going to add 2 integers and return the sum
Args:
add_ integer(function): the function
a(int, float): the frist integer
b(int or float): the econd integer"""

def add_integer(a, b=98):
    """ this function will add two integer
        a(int, float): the frist integer
        b(int or float): the second integer"""

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return(int(a) + int(b))
    else:
        if isinstance(a, (int, float)) == False:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")


