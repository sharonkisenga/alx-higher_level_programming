#!/usr/bin/python3
"""class student list"""
class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """name last name first name age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class student"""
        return self.__dict__
