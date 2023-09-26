#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent the square."""
    def __init__(self, size=0):
        """Initialize the attr.

        args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size with a setter

        args:
            value (int): the value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calc the area of the square"""
        return self.__size ** 2
