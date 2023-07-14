#!/usr/bin/python3
""" define the model sys """


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    el = load_from_json_file("add_item.json")
except ValueError:
    el = []

save_to_json_file(el + sys.argv[1:], "add_item.json")
