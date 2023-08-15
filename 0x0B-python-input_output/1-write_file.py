#!/usr/bin/python3
"""write a string to the text file"""


def write_file(filename="", text=""):
    """text file name"""
    with open(filename, 'w') as open_file:
        open_file.write(text)
        count = open_file.tell()
    return count
