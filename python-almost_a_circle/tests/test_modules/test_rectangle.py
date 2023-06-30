#!/usr/bin/python3
"""Test Cases for Rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """tests creation of rectangle based on amounts of inputs given"""

    """2 values"""

    def test_rectangle_creation_1(self):
        rectangle_1 = Rectangle(1, 2)
        self.assertEqual(rectangle_1.width, 1)
        self.assertEqual(rectangle_1.height, 2)

    """3 values"""

    def test_rectangle_creation_2(self):
        rectangle_2 = Rectangle(1, 2, 3)
        self.assertEqual(rectangle_2.width, 1)
        self.assertEqual(rectangle_2.height, 2)
        self.assertEqual(rectangle_2.x, 3)

    """All 4 values"""

    def test_rectangle_creation_3(self):
        rectangle_3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle_3.width, 1)
        self.assertEqual(rectangle_3.height, 2)
        self.assertEqual(rectangle_3.x, 3)
        self.assertEqual(rectangle_3.y, 4)

    """tests exceptions of rectangle"""

    def test_value(self):
        """zero and postive"""
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        """negative and postive"""
        self.assertRaises(ValueError, Rectangle, -2, 1)
        self.assertRaises(ValueError, Rectangle, 1, -2)

    """tests area method"""

    def test_area(self):
        rectangle_1 = Rectangle(3, 2)
        self.assertEqual(rectangle_1.area(), 6)

    """tests string method"""

    def test_rectangle_representation(self):
        rect_repr = str(Rectangle(5, 4, 3, 2, 1))
        result = '[Rectangle] (1) 2/3 - 4/5'
        self.assertEqual(rect_repr, result)

    """tests dictionary method"""

    def test_rectangle_to_dictionary(self):
        rect_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        result = {
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4,
            'id': 5
        }
        self.assertEqual(rect_dict, result)

    """tests update method"""

    def test_rectangle_update(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(6)
        self.assertEqual(rect.id, 6)

    def test_rectangle_update_2(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(6, 10, 50)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 50)


if __name__ == "__main__":
    unittest.main()
