#!/usr/bin/python3
def roman_to_int(roman_string):

    roman = {"I":1, "V":5, "X": 10, "L":50, "C": 100, "D": 500, "M":1000}
    vals = 0
    if roman_string:
        for letter in roman_string:
            if letter in roman_string:
                vals += roman[letter]
    return vals
