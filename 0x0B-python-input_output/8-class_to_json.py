#!/usr/bin/python3
"""A "Class to JSON" module."""


def class_to_json(obj):
    """
    Convert the attrs of a class instance to a dict suitable for JSON.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing the attributes of the class instance.
    """
    dict_description = {}

    # Iterate through the attributes of the object
    for attr_name in dir(obj):
        # Get the value of the attribute
        attr_value = getattr(obj, attr_name)

        # Exclude callable objects and special attributes/methods
        if not callable(attr_value) and not attr_name.startswith("__"):
            dict_description[attr_name] = attr_value

    return dict_description
