#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    arr = my_list[::-1]
    for i in range(len(arr)):
        print("{:d}".format(arr[i]))
