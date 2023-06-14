#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0
    upper = roman_string.upper()
    for i in range(len(upper)):
        if roman.get(upper[i], 0) == 0:
            return (0)

        if (i != (len(upper) - 1) and roman[upper[i]] < roman[upper[i + 1]]):
            num += roman[upper[i]] * -1

        else:
            num += roman[upper[i]]
    return (num)