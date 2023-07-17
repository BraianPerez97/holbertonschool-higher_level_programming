#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Rectangle class

    """

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """string function for rectangle
        Returns:
            width, height
        """
        return ('[Rectangle]' + str(self.__width)) + '/' + str(self.__height)

    def area(self):
        """ Calculate area of rectangle"""
        return self.__width * self.__height
