#!/usr/bin/python3
"""python OOP: inheritance
"""

def lookup(obj):

    """function that returns the list of available attributes
    and methods of an object

    args:
        obj: instance of the class

    Returns:
        List of attributes
    """
    return dir(obj)
