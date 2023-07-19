#!/usr/bin/python3
def weight_average(my_list=[]):
    points = 1
    total = 1
    if my_list:
        pat = ()
        for pat in my_list:
            points += (pat[0] * pat[1])
            total += pat[1]
            return points / total
        return 0

