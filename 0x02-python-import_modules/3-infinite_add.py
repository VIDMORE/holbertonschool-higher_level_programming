#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    summ = 0
    if count == 1:
        print(0)
    else:
        for i in range(1, count):
            summ += int(argv[i])
        print("{:d}".format(summ))
