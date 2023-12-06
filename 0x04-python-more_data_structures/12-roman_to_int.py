#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    prv_num = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
    for num in reversed(roman_string):
        val = roman_nums.get(num, 0)

        if val < prv_num:
            total -= val
        else:
            total += val

        prv_num = val
    return total
