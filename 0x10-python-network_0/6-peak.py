#!/usr/bin/python3
""" finds a peak in a list of unsorted integers"""
def find_peak(list_of_integers):
    """ find the peak """
    k = list_of_integers
    peaks = []
    for e in range(1, len(list_of_integers)-1):
        if k[e] > k[e-1] and k[e] > k[e+1]:
            peaks.append(l[e])
        if k[e] < k[e-1] and k[e] < k[e+1]:
            peaks.append(k[e])
        if k[e] == k[e-1] and k[e] == k[e+1]:
            peaks.append(l[e])
    if len(peaks) == 0:
        return None
    return max(peaks)
