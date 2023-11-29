#!/usr/bin/python3
for x in range(00, 99+1):
    print('{:02d}' .format(x), end='\n' if x == 99 else ', ')
