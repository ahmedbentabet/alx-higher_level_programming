#!/usr/bin/python3
import unittest
from models.base import Base


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
        result = Base.to_json_string([{'id': 1, 'name': 'med'}, {'id': 2, 'name': 'Jane'}])

        # Define the expected JSON string
        expected_result = '[{"id": 1, "name": "med"}, {"id": 2, "name": "Jane"}]'

        # Compare the result with the expected JSON string
        self.assertEqual(result, expected_result)
