#!/usr/bin/python3

"""declare a class Rectangle"""


class Rectangle:
    """define a class Rectangle"""
    def __init__(self, width=0, height=0):
        """ func that init the attr
        args:
            width (int): the width of rectangel
            height (int): the height of rectangel
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """get width

        Returns:
            width of rectangel
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set height
        args:
            value (int): the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height

        Returns:
            height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set value of height

        args:
            value (int): value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
