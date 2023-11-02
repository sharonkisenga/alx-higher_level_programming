#!/usr/bin/python3
""" finds a peak in a list of unsorted integers"""
def find_peak(list_of_integers):
    """find peak list """
    peak_i = None
    for ele in list_of_integers:
        if peak_i is None or peak_i < ele:
            peak_i = ele
    return peak_i
