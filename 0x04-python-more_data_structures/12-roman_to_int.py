#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return None
    rom = {}
    rom["I"] = 1
    rom["V"] = 5
    rom["X"] = 10
    rom["L"] = 50
    rom["C"] = 100
    rom["D"] = 500
    rom["M"] = 1000
    res = rom[roman_string[0]]
    temp =0
    for i in range(1, len(roman_string)):
        if rom[roman_string[i]] > rom[roman_string[i - 1]] and >= 0:
            res -= rom[roman_string[i]]
        elif rom[roman_string[i]] < rom[roman_string[i - 1]] <= 0:
            res += rom[roman_string[i]]
        else:
            res += rom[roman_string[i]]
        if res < 0:
            res *= -1
    return res
