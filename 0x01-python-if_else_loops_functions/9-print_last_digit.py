#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        ya_mwishow = number % 10
    else:
        ya_mwishow = number % -10
        ya_mwishow *= -1

    print("{:d}".format(ya_mwishow), end='')
    return (ya_mwishow)
