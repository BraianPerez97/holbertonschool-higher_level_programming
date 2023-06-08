#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    name_key = ""
    max_score = 0
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            name_key = key
    return (name_key)
