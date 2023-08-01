#!/usr/bin/python3
""" defines a square by: (based on 1-square.py) """

class Square:
    """ define class square """
     def __init__(self, size=0):
         """ define class square """
        if type(size) != int:
            """ class square """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ class square """
            raise ValueError("size must be >= 0")
        else:
            """ class square """
            self.__size = size
