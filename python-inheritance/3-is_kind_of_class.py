#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of class or if the object is an instance of a class that inherited from
    """
    if isinstance(a_class, type) or issubclass(type(obj), a_class):
        return True

    elif not isinstance(a_class, type):
        raise TypeError("a_class type must be type")

    else:
        return False
