#!/usr/bin/python3
"""  a class Square that defines a square by: (based on 2-square.py) """
class Square:
    """ class square """
    def __init__(self, size=0):
        """ class square """
        if type(size) != int:
            """ class square """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ class square """
            raise ValueError("size must be >= 0")
        else:
            """ class square """
            self.__size = size

    def area(self):
        """ class square """
        return self.__size * self.__size
