#!/usr/bin/python3
""" define a class to json function """


def class_to_json(obj):
    """ return a dicts from an object """
    attr = vars(obj)
    dicts = {}

    for key, value in attr.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dicts[key] = value
    return dicts
