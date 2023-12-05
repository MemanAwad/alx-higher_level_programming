#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """function to read files"""

    with open(filename) as f:
        for line in f:
            print(line, end="")
