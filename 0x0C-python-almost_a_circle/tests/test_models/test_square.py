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
