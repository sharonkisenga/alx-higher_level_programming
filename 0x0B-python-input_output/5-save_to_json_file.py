#!/usr/bin/python3
"""write an object to a text"""
import json
def save_to_json_file(my_obj, filename):
    """obect text"""
    with open(filename, 'w') as open_file:
        open_file.write(json.dumps(my_obj))
