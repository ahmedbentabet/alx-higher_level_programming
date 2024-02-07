#!/usr/bin/python3
"""fhhhhhhhhh"""


class Student:
    """fdsfdfdfdf"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        dict_description = {}

        # Iterate through the attributes of the object
        for attr_name in dir(self):
            # Get the value of the attribute
            attr_value = getattr(self, attr_name)

            # Exclude callable objects and special attributes/methods
            if not callable(attr_value) and not attr_name.startswith("__"):
                dict_description[attr_name] = attr_value

        return dict_description
