#!/usr/bin/python3
"""define a inherits from function"""


def inherits_from(obj, a_class):
    """ return true if obj is subclass of a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
