#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy_dic = a_dictionary
    for key in sorted(copy_dic.keys()):
        print("{}: {}".format(key, copy_dic[key]))

