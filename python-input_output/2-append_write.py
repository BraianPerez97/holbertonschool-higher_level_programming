#!/usr/bin/python3
""" Python: Input and Output"""


def append_write(filename="", text=""):
    """Function to append a string to the end of a text file and return
      the number of charaters appeneded"""
    with open(filename, "a", encoding="utf-8") as f:
        num_char = f.write(text)
    return num_char
