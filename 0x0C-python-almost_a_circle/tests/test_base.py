#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_constructor_without_id(self):
        obj = Base()
        self.assertIsNotNone(obj.id)

# if __name__ == '__main__':
#     unittest.main()
