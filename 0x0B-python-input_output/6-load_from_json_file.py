#!/usr/bin/python3
"""define a load from json file """
import json


def load_from_json_file(filename):
    """ create object from a json file """
    with open(filename, 'r') as fl:
        json_str = fl.read()
        obj = json.loads(json_str)
        return obj
