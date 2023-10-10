#!/usr/bin/python3
import json

"""define a save to json file"""


def save_to_json_file(my_obj, filename):
    """write obj to a text file using json representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj, indent=4)
        f.write(json_str)
        return True
