#!/usr/bin/python3
"""drived class"""

class MyList(list):
    """ my list class"""
    
    def print_sorted(self):
        print(sorted(self))
