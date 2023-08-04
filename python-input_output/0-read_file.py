#!/usr/bin/python3
"""Python: Input and Output"""


def read_file(filename=""):
    """Open file for reading"""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
