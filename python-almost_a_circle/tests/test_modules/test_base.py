#!/usr/bin/pyhton3
import unittest
import calc

"""Module Comment

    Test casses: a test class that inherits the 'unittest.Testcase'
"""


class TestCalc(unittest.TestCase):

    """"must start with 'test_' (otherwise: "add_test") it gets skipped

    Example: testing the add Functions
    """

    def test_add(self):

        """built-in functions documantation are online ('sefl.assetExample')
            Edge Casses:
                Errors could happen within this function
        """

        """Edge Case: two positves"""
        self.assertEqual(calc.add(10, 5), 15)

        """Edge Case: one positive & one negative"""
        self.assertEqual(calc.add(-1, 1), 0)

        """Edge Case: two negatives"""
        self.assertEqual(calc.add(-1, -1) -2)


    def test_subtract(self):
        """Edge Case: two positves"""
        self.assertEqual(calc.subtract(10, 5), 5)

        """Edge Case: one positive & one negative"""
        self.assertEqual(calc.subtract(-1, 1), -2)

        """Edge Case: two negatives"""
        self.assertEqual(calc.subtract(-1, -1), 0)


    def test_multiply(self):
            """Edge Case: two positves"""
            self.assertEqual(calc.multiply(10, 5), 50)

            """Edge Case: one positive & one negative"""
            self.assertEqual(calc.multiply(-1, 1), -1)

            """Edge Case: two negatives"""
            self.assertEqual(calc.multiply(-1, -1), 1)


    def test_divide(self):

            """Edge Case: two positves"""
            self.assertEqual(calc.divide(10, 5), -1)

            """Edge Case: one positive & one negative"""
            self.assertEqual(calc.divide(-1, 1), -1)

            """Edge Case: two negatives"""
            self.assertEqual(calc.divide(-1, -1), 1)

            """Edge Case: floor division"""
            self.assertEqual(calc.divide(5, 2), 2.5)

            """Testing Exception:

                Context Manager
            """

            with self.assertRaise(ValueError):
                calc.divide(10, 0)
