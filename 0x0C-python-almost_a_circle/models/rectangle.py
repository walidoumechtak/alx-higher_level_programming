#!/usr/bin/python3
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
    def getWidth(self):
        """get the width"""
        return self.__width

    @getWidth.setter
    def setWidth(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("wdith must be an integer")
        self.__wdith = value

