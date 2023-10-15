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

    @property
    def getHeight(self):
        """get the height"""
        return self.__height

    @getHeight.setter
    def setHeight(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def getX(self):
        """get the x"""
        return self.__x
    
    @getX.setter
    def setX(self.value):
        """set the X"""
        if not isinstance(self, value):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def getY(self):
        """get the Y"""
        return self.__y

    @getY.setter
    def setY(self, value):
        """set The Y"""
        if not isinstance(self, value):
            raise TypeError("y must be anintger")
        self.__y = value
