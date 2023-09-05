#!/usr/bin/python3
def uppercase(str):
    for c in str:
        asci = ord(c)
        asci -= 32
        newc = chr(asci)
        print("{}".format(newc), end='')
    print()
