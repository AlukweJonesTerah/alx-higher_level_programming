#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i + 1, 10):
        print('{}{}'.format(i, x), end='\n' if i == 8 and x == 9 else ', ')
