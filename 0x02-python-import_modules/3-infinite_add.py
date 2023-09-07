#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    sum = 0
    for i in range(1, size):
        sum += int(sys.argv[i])
    print("{}".format(sum))
