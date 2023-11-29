#!/usr/bin/python3
def upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(str):
    new1 = ""
    for char in str:
        new1 += "%c" % upper(char)
    print("{:s}".format(new1))
