#!/usr/bin/python3
""" json losd, add, and save"""
import json
import os.path
import sys
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

listt = []

if os.path.exists("add_item.json"):
    listt = load_from_json_file("add_item.json")

for strr in argv[1:]:
    listt.append(strr)

save_to_json_file(listt, "add_item.json")
