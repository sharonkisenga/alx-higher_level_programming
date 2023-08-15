#!/usr/bin/python3
"""create an object"""
import json
def load_from_json_file(filename):
    """load json file"""
     with open(filename, 'r') as open_file:
        return json.load(open_file)
