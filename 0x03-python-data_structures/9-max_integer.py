#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    n = len(my_list)
    for i in range(n):
        for  j in range(n - i -1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j+1] = my_list[j + 1], my_list[j]
    max_value = my_list[-1]
    return max_value
