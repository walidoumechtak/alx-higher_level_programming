#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newa = []
    for ele in my_list:
            if ele == search:
                newa.append(replace)
            else:
                newa.append(ele)
    return newa
