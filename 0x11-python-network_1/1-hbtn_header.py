#!/usr/bin/python3
"""Write a Python script that takes in a URL"""
import urllib.request as ur
import sys

try:
    req = ur.Request(sys.argv[1])
    with ur.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
except BaseException:
    pass
