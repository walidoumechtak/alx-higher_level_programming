#!/usr/bin/python3

""" define a from json to string function """
import json


def from_json_string(my_str):
    """ object represented by a JSON string"""
    obj = json.loads(my_str)
    return obj
