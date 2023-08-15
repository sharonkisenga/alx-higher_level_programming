#!/usr/bin/python3

"""
write a class square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle square"""

    def __init__(self, size):
        """square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """find the area"""
        return self.__size ** 2

    def __str__(self):
        """find string """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
