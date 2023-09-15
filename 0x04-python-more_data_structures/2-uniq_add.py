#!/usr/bin/python3
def uniq_add(my_list=[]):
    sums = 0
    arr = []
    for i in my_list:
        if my_list.count(i) < 2:
            sums += i
        else:
            if i not in arr:
                arr.append(i)
    for j in arr:
        sums += j
    return sums
