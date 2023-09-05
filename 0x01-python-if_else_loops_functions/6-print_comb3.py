#!/usr/bin/python3
strg = ""
for i in range(0, 9):
    for j in range(i, 10):
        strg = str(i) + str(j)
        if i == 8 and j == 9 and i != j:
            print("{}".format(strg))
        elif i != j:
            print("{}, ".format(strg), end='')
