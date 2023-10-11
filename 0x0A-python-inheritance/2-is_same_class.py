#!/usr/bin/python3
"""define a isSameClass function"""


def is_same_class(obj, a_class):
    """return ture if is it an instance of a_class
    Args:
        obj (object): the object should check
        a_class (object): the class to check with
    Returns:
        True or False
    """
    if type(obj) == a_class:
        return True
    return False
