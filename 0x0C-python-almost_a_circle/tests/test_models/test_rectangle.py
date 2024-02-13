#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Explicitly reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_id(self):
        self.r1 = Rectangle(10, 2)
        self.assertEqual(self.r1.id, 1)

        self.r2 = Rectangle(2, 10)
        self.assertEqual(self.r2.id, 2)

        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.r3.id, 12)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 2)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -1)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 0, "invalid")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 0, -1)

    def test_valid_values(self):
        r = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_area_regular_case(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_area_square_case(self):
        r = Rectangle(4, 4)
        self.assertEqual(r.area(), 16)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        r = Rectangle(10, 2, 3, 4, 1)
        expected_result = "[Rectangle] (1) 3/4 - 10/2"
        self.assertEqual(str(r), expected_result)
