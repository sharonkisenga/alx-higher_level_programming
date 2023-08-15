#!/usr/bin/python3
"""read a utf8"""
def read_file(filename=""):
    """filename"""
    with open(filename) as open_file:
        contents = open_file.read()
    print(contents, end="")
