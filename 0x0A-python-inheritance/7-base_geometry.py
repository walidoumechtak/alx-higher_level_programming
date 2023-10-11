#!/usr/bin/python3
"""define a baseGeometry class"""


class BaseGeometry:
    """Implemtn the class BaseGeometry"""
    def area(self):
        """define an area that throw an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(value))
