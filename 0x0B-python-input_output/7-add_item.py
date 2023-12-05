#!/usr/bin/python3
""" json losd, add, and save"""
import sys

if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        listt = load_from_json_file("add_item.json")
    except FileNotFoundError:
        listt = []
    listt.extend(sys.argv[1:])
    save_to_json_file(listt, "add_item.json")
