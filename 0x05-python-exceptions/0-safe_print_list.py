#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list), ends="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count