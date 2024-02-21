#!/usr/bin/python3
"""This module defines the Base class."""
import json
import csv


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

        # Check if 'size' is a key in the dictionary, indicating it's a Square
        if 'size' in dictionary:
            dummy_instance = cls(size=1)  # for a Square
        else:
            dummy_instance = cls(width=1, height=1)  # for a Rectangle

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id, obj.width, obj.height,
                        obj.x, obj.y
                        ])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        obj_list = []

        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj_list.append(cls(
                            int(row[0]), int(row[1]), int(row[2]),
                            int(row[3]), int(row[4])
                            ))
                    elif cls.__name__ == "Square":
                        obj_list.append(cls(
                            int(row[0]), int(row[1]),
                            int(row[2]), int(row[3])
                            ))

            return obj_list

        except FileNotFoundError:
            return obj_list

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
