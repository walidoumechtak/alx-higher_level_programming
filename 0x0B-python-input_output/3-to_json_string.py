#!/usr/bin/python3

""" define a to json string function """
import json


def to_json_string(my_obj):
    """ generate a json format from a string"""
    json_str = json.dumps(my_obj)
    return json_str
