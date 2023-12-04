#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = len(my_list)
    twos = []
    for i in range(n):
        if my_list[i] % 2 == 0:
            twos.append(True)
        else:
            twos.append(False)
    return twos
