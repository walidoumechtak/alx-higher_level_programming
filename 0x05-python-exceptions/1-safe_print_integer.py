#!/usr/bin/python3
def safe_print_integer(value):
    cpt = False
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            cpt = True
    except ValueError:
        print("error")
    return cpt
