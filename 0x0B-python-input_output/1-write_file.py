#!/usr/bin/python3
""" write ti a foole module"""


def write_file(filename="", text=""):
    """function to write in a file"""

    with open(filename, "w") as f1:
        return (f1.write(text))
