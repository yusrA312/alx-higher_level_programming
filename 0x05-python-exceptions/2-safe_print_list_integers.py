#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    # Print the first x elements of a list that are
    t = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            t += 1
        except (ValueError, TypeError):
            pass
    print("")
    return t
