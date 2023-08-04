#!/usr/bin/python3
"""Python: Input and Output"""


def write_file(filename="", text="utf-8"):
    """Write string to a text file. and returns the num of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        num_char = f.write(text)
    return num_char
