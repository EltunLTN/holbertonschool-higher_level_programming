#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    total = 0
    for i in range(len(roman_string)):
        current = roman[roman_string[i]]
        if i < len(roman_string) - 1:
            next_val = roman[roman_string[i + 1]]
            if current < next_val:
                total -= current
                continue
        total += current
    return total
