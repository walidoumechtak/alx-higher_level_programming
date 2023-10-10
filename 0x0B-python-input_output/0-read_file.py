#!/usr/bin/python3

""" define a read_file function"""


def read_file(filename=""):
    """print the content of filename file"""
    with open(filename, 'r', encoding='utf-8') as file:
        cont = file.read()
        print(cont, end='')
