#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cpt = 0
    try:
        for i in my_list:
            if x > 0:
                print("{:d}".format(i))
                x = x - 1
                cpt = cpt + 1
    except ValueError:
        print("error")
    return cpt
