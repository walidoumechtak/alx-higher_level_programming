#!/usr/bin/python3
"""define a class Base"""


class Base:
    """body of the Base class"""
    
    __nb_objects = 0
    def __init__(self, id=None):
        """defin init funct
        
        Args:
            id (int): the id of object
        """
        if id not None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
