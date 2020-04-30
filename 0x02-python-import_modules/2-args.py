#!/usr/bin/python3
from sys import argv

count = len(argv)

if count == 1:
    print("0 arguments.")
elif count == 2:
    print("1 argument:")
    print("1: {:s}".format(argv[1]))
else:
    print("{} arguments:".format(count - 1))
    for i in range(1, count):
        print("{:d}: {:s}".format(i, argv[i]))
