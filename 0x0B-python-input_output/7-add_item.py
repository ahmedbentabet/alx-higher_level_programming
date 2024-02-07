#!/usr/bin/python3
""" Add all arguments to a Python list, and then save them to a file. """
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
new_list = []
new_list.extend(args)

if os.path.isfile("add_item.json"):
    items = load_from_json_file("add_item.json")
else:
    items = []

items.extend(new_list)
save_to_json_file(items, "add_item.json")
