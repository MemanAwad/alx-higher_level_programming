#!/usr/bin/python3
"""json module """


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using json"""

    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)
