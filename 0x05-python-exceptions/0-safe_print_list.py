#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cpt = 0
        for i in my_list and x > 0:
            print("{:d}".format(i))
            x--
            cpt++
    except ValueError:
        print("error")
    return cpt
