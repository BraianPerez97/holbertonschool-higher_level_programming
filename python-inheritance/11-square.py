#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):

    """
    square subclass inheriting from rectangle

    """

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """string that prints width and height
        """
        return ('[Square]' + str(self.__size) + '/' + str(self.__size))

    def area(self):
        """returns area of Square
        """
        return (self.__size ** 2)#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square from Rectangle class """
    def __init__(self, size):
        """ Method that initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()

    def __str__(self):
        """ Special method that returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
