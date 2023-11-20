#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except TypeError as ty:
        print("Exception:", ty.exe, file=sys.stderr)
    except ValueError as va:
        print("Exception:", va, file=sys.stderr)
    return False
