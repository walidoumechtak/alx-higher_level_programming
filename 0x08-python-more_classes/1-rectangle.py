#!/usr/bin/python3

"""declare a class Rectangle"""


class Rectangle:
    """define class rectangle"""
    def __init__(self, width=0, height=0):
        """ func that init the attr
        args:
            width (int): the width of rectangel
            height (int): the height of rectangel
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
    
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
        self.__height = value
