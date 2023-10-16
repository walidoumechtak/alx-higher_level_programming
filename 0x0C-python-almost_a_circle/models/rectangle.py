#!/usr/bin/python3
from models.base import Base
"""declare a Rectangle class"""


class Rectangle(Base):
    """define a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define init functinon

        Args:
            width (int): the width of rectangel
            height (int): the height of retangel
            x (int): x
            y (int): y
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__wdith = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """set the X"""
        if not isinstance(self, value):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set The Y"""
        if not isinstance(self, value):
            raise TypeError("y must be anintger")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle"""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end='')
            print("")
