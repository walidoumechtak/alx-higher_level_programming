#!/usr/bin/python3
strg = ""
for i in range(0, 100):
    strg = str(i).zfill(2)
    if i != 99:
        print("{}, ".format(strg), end='')
    else:
        print("{}".format(strg))
