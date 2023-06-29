#!/usr/bin/python
""" file to be tested"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

"""(hardcided typo bug for edge case: floor division) current test will run because thest cases are whole numbers"""
def divide(x, y):
    return x // y
""" To catch this edge case"""
def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x // y
