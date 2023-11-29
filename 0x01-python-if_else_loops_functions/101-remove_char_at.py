#!/usr/bin/python3
def remove_char_at(str, n):
    a = 0
    str2 = ""
    for ch in str:
        if a != n:
            str2 += ch
        a += 1
    return str2
