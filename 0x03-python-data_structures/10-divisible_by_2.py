#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    arr = []
    for i in my_list:
        if i % 2 == 0:
            arr.append(True)
        else:
            arr.append(False)
    return arr
