#!/usr/bin/python3
"""Test Cases for Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """tests creation of square based on amounts of inputs given"""

    """success"""

    def test_square_creation_1(self):
        square_1 = Square(1)
        self.assertEqual(square_1.size, 1)

    """2 values"""

    def test_square_creation_1(self):
        square_2 = Square(1, 2)
        self.assertEqual(square_2.size, 1)
        self.assertEqual(square_2.x, 2)

    """All 3 values"""

    def test_square_creation_1(self):
        square_3 = Square(1, 2, 3)
        self.assertEqual(square_3.size, 1)
        self.assertEqual(square_3.x, 2)
        self.assertEqual(square_3.y, 3)

    """tests exceptions of square"""

    def test_value(self):
        """zero and negative"""
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -2)

    """tests string method"""

    def test_square_representation(self):
        sq_repr = str(Square(4, 3, 2, 1))
        result = '[Square] (1) 3/2 - 4'
        self.assertEqual(sq_repr, result)

    """tests dictionary method"""

    def test_square_to_dictionary(self):
        sq_dict = Square(1, 2, 3, 4).to_dictionary()
        result = {
            'size': 1,
            'x': 2,
            'y': 3,
            'id': 4
        }
        self.assertEqual(sq_dict, result)

    """tests update method"""

    def test_square_update(self):
        sq = Square(4, 3, 2, 1)
        sq.update(5)
        self.assertEqual(sq.id, 5)

    def test_square_update_2(self):
        sq = Square(4, 3, 2, 1)
        sq.update(6, 10, 50)
        self.assertEqual(sq.id, 6)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 50)


if __name__ == "__main__":
    unittest.main()
