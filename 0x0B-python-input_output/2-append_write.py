#!/usr/bin/python3

""" define a append wirte functin"""


def append_write(filename="", text=""):
    """ append a string to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        nums = file.write(text)
        return nums
