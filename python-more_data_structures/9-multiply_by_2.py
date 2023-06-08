#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    new_d = {key: (value * 2) for (key, value) in new_d.items()}
    return (new_d)
