#!/usr/bin/python3
""" Get JSON representation of an object """


import json

def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string). """

    object = json.dumps(my_obj)
    return object
