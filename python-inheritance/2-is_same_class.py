#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""

def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of class
    """
    if isinstance(a_class, type):
        return (type(obj) is a_class)
    else:
        return (type(obj) is not a_class)
