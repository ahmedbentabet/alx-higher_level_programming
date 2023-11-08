#!/usr/bin/python3
""" Add all arguments to a Python list, and then save them to a file. """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
new_list = []
for arg in args:
    new_list.append(arg)

list_from_json = load_from_json_file("add_item.json")
save_to_json_file(new_list[1:], "add_item.json")
list_from_json.extend(new_list[1:])
save_to_json_file(list_from_json, "add_item.json")
