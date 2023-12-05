#!/usr/bin/python3
"""appent ot a file module"""


def append_write(filename="", text=""):
    """ function to append text to the file content"""

    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
