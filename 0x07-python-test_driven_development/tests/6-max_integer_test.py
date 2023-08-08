#!/usr/bin/python3
"""write the unitest function"""
def max_integer(list=[]):
    """the unitest function"""
if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
~                          
