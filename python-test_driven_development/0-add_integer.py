#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""


def add_integer(a, b=98):
    """"Accept two values, whether they are an int or a float,
      cast them to integers before adding."""
    if not isinstance(a, (int,float)):
        raise TypeError("a must be and integer")
    elif not isinstance(b, (int,float)):
        raise TypeError("b must be and integer")
    else:
        return int(a) + int(b)
