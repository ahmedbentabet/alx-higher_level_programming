#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        # Reset the number of objects before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_square_attributes(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_size_getter_setter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)

        with self.assertRaises(TypeError):
            s.size = "invalid"

        with self.assertRaises(ValueError):
            s.size = 0

    def test_square_str_representation(self):
        s = Square(5, 2, 3, 7)
        expected_output = "[Square] (7) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_update_with_args(self):
        r = Square(1, 2, 3, 4)
        r.update(10, 20, 30, 40)

        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)

    def test_update_with_kwargs(self):
        r = Square(1, 2, 3, 4)
        r.update(id=10, width=20, height=30, x=40, y=50)

        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_to_dictionary(self):
        # Create an instance of the Square class
        square_instance = Square(id=1, size=10, x=2, y=1)

        # Call the to_dictionary method
        result_dict = square_instance.to_dictionary()

        # Define the expected dictionary based on the instance attributes
        expected_dict = {
            'id': 1,
            'size': 10,
            'x': 2,
            'y': 1
        }

        # Compare the result with the expected dictionary
        self.assertDictEqual(result_dict, expected_dict)
