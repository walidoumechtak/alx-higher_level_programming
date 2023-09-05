#!/usr/bin/python3
c = ""
for i in range(97, 122 + 1):
    if i != 101 and i != 113:
        c += chr(i)
print("{}".format(c), end='')
