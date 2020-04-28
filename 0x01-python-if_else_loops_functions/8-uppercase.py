#!/usr/bin/python3
def uppercase(str):
    for char in str:
        letter = ord(char)
        print("{}".format(chr(letter - 32)) if letter >= 97 and letter <= 122 else char, end="")
    print("")
