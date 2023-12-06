#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    tmp = my_dict.copy()

    for key, v in tmp.items():

        if value == v:

            my_dict.pop(key)

    return my_dict
