#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """find the email"""
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html_str = html.decode('utf-8')
    print(html_str)
