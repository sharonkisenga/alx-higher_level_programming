#!/usr/bin/python3
"""class rectangle"""
class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """find width"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """find width"""
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        """find height"""
        return self.__height

    @height.setter
    def height(self, HeightValue):
        """find height"""
        if type(HeightValue) != int:
            raise TypeError("height must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = HeightValue
