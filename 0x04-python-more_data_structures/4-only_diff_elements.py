#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    arr = []
    for ele in set_1:
        if ele not in set_2:
            arr.append(ele)
    for ele2 in set_2:
        if ele2 not in set_1:
            arr.append(ele2)
    new_set = set(arr)
    return new_set
