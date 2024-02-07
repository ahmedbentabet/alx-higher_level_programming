#!/usr/bin/python3
"""fdfsd"""


def class_to_json(obj):
    """fsdf"""

    dict_description = {}

    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if not callable(attr_value) and not attr_name.startswith("__"):
            dict_description[attr_name] = attr_value
    return dict_description
