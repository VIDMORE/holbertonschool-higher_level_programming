#!/usr/bin/python3
def append_write(filename="", text=""):

    nb_characters = 0

    with open(filename, 'a', encoding="utf-8") as file:
        nb_characters = file.write(text)

    return nb_characters
