#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = dict(sorted(a_dictionary.items()))
    obj = new_dic.items()
    for key, value in obj:
        print("{}: {}".format(key, value))
