#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newa = []
    for ele in my_list:
        newe = []
        for n in range(0, range(0, len(ele))):
            if ele[n] == search:
                newe.append(replace)
            else:
                newe.apped(ele[n])
        newa.append(newe)
    return newa
