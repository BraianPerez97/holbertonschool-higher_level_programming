#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""

class BaseGeometry:

    """
    Base Geometry class

    Public Instance
    """

    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be a validator".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
