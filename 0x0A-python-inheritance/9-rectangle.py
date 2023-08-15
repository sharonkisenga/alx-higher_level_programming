#!/usr/bin/python3

"""
write a class rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """find the area"""
        return self.__width * self.__height

    def __str__(self):
        """get string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
