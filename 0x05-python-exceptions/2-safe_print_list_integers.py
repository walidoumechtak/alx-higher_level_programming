#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cpt = 0
    try:
        for i in my_list:
            if (x > 0 and isinstance(i, int)):
                cpt = cpt + 1
                x = x - 1
                print("{:d}".format(i), end='')
        print("")
    except ValueError:
        print("error")
    return cpt
