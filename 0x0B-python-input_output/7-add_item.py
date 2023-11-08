#!/usr/bin/python3
""" Add all arguments to a Python list, and then save them to a file. """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
new_list = []
for arg in args:
    new_list.append(arg)

items = load_from_json_file("add_item.json")
items.extend(new_list[1:])
save_to_json_file(items, "add_item.json")
