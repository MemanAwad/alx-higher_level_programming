#!/usr/bin/python3
import sys

def safe_function(fct, *args):

    try:
        n = fct(args[0], args[1])
        return n
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None

