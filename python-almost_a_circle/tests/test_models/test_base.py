#!/usr/bin/python3
"""Test Cases for Rectangle"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base class tests"""
    """tests id"""

    def test_id(self):
        base_1 = Base()
        self.assertEqual(base_1.id, 1)
        base_2 = Base()
        self.assertEqual(base_2.id, 2)
        base_3 = Base(12)
        self.assertEqual(base_3.id, 12)

    """tests str to json"""

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    """tests if exists"""

    def test_to_json_string_exists(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    """test json to str"""

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    """tests if exist"""

    def test_to_json_string_exists(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')


if __name__ == "__main__":
    unittest.main()
