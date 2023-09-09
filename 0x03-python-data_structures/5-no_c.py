#!/usr/bin/python3
def no_c(my_string):
    res = ""
    for i in my_string:
        res = "".join([char for char in my_string if char != "c"])
    for i in res:
        res = "".join([char for char in res if char != "C"])
    return res
