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
