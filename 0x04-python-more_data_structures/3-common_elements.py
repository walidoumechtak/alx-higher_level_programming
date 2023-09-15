#!/usr/bin/python3
def common_elements(set_1, set_2):
    sets = []
    for ele in set_1:
        if ele in set_2:
            sets.append(ele)
    new_set = set(sets)
    return new_set
