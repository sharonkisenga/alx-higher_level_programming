#!/usr/bin/python3

"""
write a function that add new attribute
"""


def add_attribute(obj, key, value):
    """add attribute abj key value"""
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, key):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
