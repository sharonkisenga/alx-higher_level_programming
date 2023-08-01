#!/usr/bin/python3
class Square:
    """ defines a square by: (based on 3-square.py) """
    def __init__(self, size=0):
        """ defines a square by: (based on 3-square.py) """
        if type(size) != int:
            """ defines a square by: (based on 3-square.py) """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ defines a square by: (based on 3-square.py) """
            raise ValueError("size must be >= 0")
        else:
            """ defines a square by: (based on 3-square.py) """
            self.__size = size

    @property
    def size(self):
        """ defines a square by: (based on 3-square.py) """
        return self.__size

    @size.setter
    def size(self, value):
        """ defines a square by: (based on 3-square.py) """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            """ defines a square by: (based on 3-square.py) """
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ defines a square by: (based on 3-square.py) """
        return self.__size * self.__size
