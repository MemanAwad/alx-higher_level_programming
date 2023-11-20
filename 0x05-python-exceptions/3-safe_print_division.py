#!/usr/bin/python3
def safe_print_division(a, b):
    quo = 0
    try:
        quo = a / b
    except ZeroDivisionError:
        return None
    finally:
        if (b == 0):
            quo = None
        print("Inside result: {}".format(quo))
        return quo
