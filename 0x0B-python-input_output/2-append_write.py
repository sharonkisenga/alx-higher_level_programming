#!/usr/bin/python3
"""append a string"""
def append_write(filename="", text=""):
    """append a string"""
    with open(filename, 'a') as open_file:
        count = open_file.write(text)
    return count
