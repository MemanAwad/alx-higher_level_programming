#!/usr/bin/python3
""" json losd, add, and save"""
import sys
import json


try:
    with open("add_item.json", "r", encoding="utf-8") as f:
        listt = json.load(f)
except FileNotFoundError:
    listt = []
listt.extend(sys.argv[1:])
with open(filename, "w", encoding="utf-8") as myfile:
    json.dump(listt, "add_item.json")
