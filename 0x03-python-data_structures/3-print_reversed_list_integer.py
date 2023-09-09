#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    arr = my_list[::-1]
    for i in arr:
        print("{:d}".format(i))
