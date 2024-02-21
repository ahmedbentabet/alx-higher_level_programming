#!/usr/bin/python3
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        # Explicitly reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_id(self):
        self.b1 = Base()
        self.assertEqual(self.b1.id, 1)

        self.b2 = Base()
        self.assertEqual(self.b2.id, 2)

        self.b3 = Base(12)
        self.assertEqual(self.b3.id, 12)

        self.b4 = Base()
        self.assertEqual(self.b4.id, 3)  # 2 + 1 = 3

    def test_to_json_string_empty(self):
        # Call the to_json_string method with an empty list
        result = Base.to_json_string([])

        # Define the expected result
        expected_result = "[]"

        # Compare the result with the expected string
        self.assertEqual(result, expected_result)

    def test_to_json_string_none(self):
        # Call the to_json_string method with None
        result = Base.to_json_string(None)

        # Define the expected result
        expected_result = "[]"

        # Compare the result with the expected string
        self.assertEqual(result, expected_result)

    def test_to_json_string_non_empty(self):
        # Call the to_json_string method with a non-empty list of dictionaries
        result = Base.to_json_string([
            {'id': 1, 'name': 'med'},
            {'id': 2, 'name': 'SO'}
            ])

        # Define the expected JSON string
        expected_result = '[{"id": 1, "name": "med"}, {"id": 2, "name": "SO"}]'

        # Compare the result with the expected JSON string
        self.assertEqual(result, expected_result)

    def test_save_to_file_with_objects(self):
        # Create instances for testing
        rectangle1 = Rectangle(4, 6)
        rectangle2 = Rectangle(3, 5)
        square1 = Square(3)
        square2 = Square(4)

        # List of instances
        list_objs = [rectangle1, rectangle2, square1, square2]

        # Call the save_to_file method
        Base.save_to_file(list_objs)

        # Assuming the file is created successfully
        file_name = f"{Base.__name__}.json"
        self.assertTrue(os.path.exists(file_name))

        # Check if the content of the file is as expected
        with open(file_name, 'r') as file:
            content = json.load(file)
            expected_content = [
                {'height': 6, 'id': 1, 'width': 4, 'x': 0, 'y': 0},  # Rectan 1
                {'height': 5, 'id': 2, 'width': 3, 'x': 0, 'y': 0},  # Rectan 2
                {'id': 3, 'size': 3, 'x': 0, 'y': 0},                # Square 1
                {'id': 4, 'size': 4, 'x': 0, 'y': 0}                 # Square 2
            ]
            self.assertEqual(content, expected_content)

    def test_save_to_file_with_empty_list(self):
        # Call the save_to_file method with an empty list
        Base.save_to_file([])

        # Assuming the file is created successfully
        file_name = f"{Base.__name__}.json"
        self.assertTrue(os.path.exists(file_name))

        # Check if the content of the file is an empty list
        with open(file_name, 'r') as file:
            content = json.load(file)
            self.assertEqual(content, [])

    def test_save_to_file_with_none(self):
        # Call the save_to_file method with None
        Base.save_to_file(None)

        # Assuming the file is created successfully
        file_name = f"{Base.__name__}.json"
        self.assertTrue(os.path.exists(file_name))

        # Check if the content of the file is an empty list
        with open(file_name, 'r') as file:
            content = json.load(file)
            self.assertEqual(content, [])
