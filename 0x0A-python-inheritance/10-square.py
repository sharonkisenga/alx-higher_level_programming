#!/usr/bin/python3

"""
write a rectangle of Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """basegeometry"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """find the area"""
        return self.__size ** 2
