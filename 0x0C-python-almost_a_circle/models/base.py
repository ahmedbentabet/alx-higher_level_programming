#!/usr/bin/python3
"""This module defines the Base class."""
import json


class Base:
    """the Base class."""

    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""

        if list_objs is None:
            list_objs = []
        file_name = f"{cls.__name__}.json"

        with open(file_name, 'w') as file:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(list_dictionaries)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""

        if json_string is None or len(json_string) == 0:
            python_list = []
        else:
            # Parse the JSON string to a Python object
            python_list = json.loads(json_string)

        return python_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set."""

        # Create a dummy instance with mandatory attributes
        dummy_instance = cls(1, 1)
        # Use the update method to apply real values from dictionary
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                list_of_dict = cls.from_json_string(json_data)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []

        # Use from_json_string and create methods to convert dicts to instances
        list_instances = [cls.create(**dict) for dict in list_of_dict]
        return list_instances

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
