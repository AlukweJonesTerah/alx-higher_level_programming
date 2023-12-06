#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for existing_key in a_dictionary:
            if existing_key == key:
                a_dictionary[existing_key] = value
    return a_dictionary
