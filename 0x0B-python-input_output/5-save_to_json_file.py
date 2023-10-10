#!/usr/bin/python3
"""define a save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """write obj to a text file using json representation"""
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
