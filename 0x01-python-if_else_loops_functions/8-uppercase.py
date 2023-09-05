#!/usr/bin/python3
def uppercase(str):
    for c in str:
        asci = ord(c)
        if (asci >= 97 and asci <= 122):
            asci -= 32
        newc = chr(asci)
        print("{}".format(newc), end='')
    print()
