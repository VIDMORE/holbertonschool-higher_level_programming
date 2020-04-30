#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    from calculator_1 import sub, add, mul, div

    count = len(argv) - 1

    if count != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        arg1 = int(argv[1])
        arg2 = argv[2]
        arg3 = int(argv[3])
        if arg2 == '+':
            print("{} + {} = {:d}".format(arg1, arg3, add(arg1, arg3)))
        elif arg2 == '-':
            print("{} - {} = {:d}".format(arg1, arg3, sub(arg1, arg3)))
        elif arg2 == '*':
            print("{} * {} = {:d}".format(arg1, arg3, mul(arg1, arg3)))
        elif arg2 == '/':
            print("{} / {} = {:d}".format(arg1, arg3, div(arg1, arg3)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
