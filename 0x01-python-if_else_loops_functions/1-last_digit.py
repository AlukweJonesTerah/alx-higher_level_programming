#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
message = 'Last digit of'
if number >= 0:
    if number % 10 == 0:
        print(f'{message} {number} is {number % 10} and is 0')
    elif number % 10 > 5:
        print(f'{message} {number} is {number % 10} and is greater than 5')
    else:
        print(f'{message} {number} is {number % 10} and is less than 6 and not 0')
else:
    if number % -10 == 0:
        print(f'{message} {number} is {number % 10} and is 0')
    else:
        print(af'{message} {number} is {number % -10} and is less than 6 and not 0')

