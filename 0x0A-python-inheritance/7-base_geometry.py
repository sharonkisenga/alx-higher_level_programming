#!/usr/bin/python3

"""
function of BaseGeometry.
"""


class BaseGeometry():
    """write a BaseGeometry"""

    def area(self):
        """base geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """write basegeometry"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
