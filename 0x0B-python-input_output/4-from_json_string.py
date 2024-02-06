#!/usr/bin/python3
""" Get an object represented by a JSON string. """
import json


def from_json_string(my_str):
    """ Returns an object (Python DS) represented by a JSON string. """

    python_obj = json.loads(my_str)
    return python_obj
