#!/usr/bin/python3

"""
write a inherits from.
"""


def inherits_from(obj, a_class):
    """function of inherit from"""
    return isinstance(obj, a_class) and type(obj) != a_class
