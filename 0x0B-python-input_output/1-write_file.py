#!/usr/bin/python3

""" define write file function"""


def write_file(filename="", text=""):
    """ write to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        nums = file.write(text)
        return nums
