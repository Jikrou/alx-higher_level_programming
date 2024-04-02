#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    out = 0
    for i in range(x):
        try:
            print("{}".format(int(my_list[i])), end="")
            out += 1
        except (TypeError, ValueError, IndexError):
            continue
    print()
    return out
