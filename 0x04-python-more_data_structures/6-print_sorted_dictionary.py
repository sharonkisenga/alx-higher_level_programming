#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for p, s in sorted(a_dictionary.items()):
        print("{}: {}".format(p, s))
