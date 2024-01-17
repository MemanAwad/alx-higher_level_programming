#!/usr/bin/python3

""" function to print a square
Args:
    print_square(functon): the print function
    size(int): the size of the square"""

def print_square(size):
    """ print square with the given size function"""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        if(i < size):
            print()
