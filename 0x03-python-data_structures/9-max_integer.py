#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    pen = my_list[0]
    for number in my_list:
        if my_list[number] > pen:
            pen = my_list[number]
            return pen
        
