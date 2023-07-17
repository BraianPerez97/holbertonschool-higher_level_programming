#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""

def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited (directly or indirectly)
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")

    return (issubclass(type(obj), a_class))
