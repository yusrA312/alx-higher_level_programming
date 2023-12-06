#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0

    d = 0

    for tup in my_list:
        num += t[0] * t[1]

        d += t[1]

    return num / d
