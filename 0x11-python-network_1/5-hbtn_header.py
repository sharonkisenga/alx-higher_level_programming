#!/usr/bin/python3
"""sends a request to the URL and displays"""
import requests
from sys import argv


if __name__ == "__main__":
    """get the requeat"""
    try:
        r_id = r.headers['X-Request-Id']
        print(r_id)
    except:
        pass
