#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    retKey = ""
    if a_dictionary is None:
        return None
    obj = a_dictionary.items()
    for key, value in obj:
        if value > max:
            max = value
            retKey = key
    return retKey
