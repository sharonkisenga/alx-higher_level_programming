#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a or (0, 0)
    b = tuple_a or (0, 0)
    if len(tuple_a) == 1:
        a = (tuple_a[0], 0)
        if len(tuple_b) == 1:
            tuple_b = tuple_b[0], 0
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
