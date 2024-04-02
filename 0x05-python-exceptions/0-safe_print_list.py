#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        out = 0
        for i in my_list:
            print("{}".format(i), end="")
            out += 1
            if out >= x:
                break
        print()
        return out
    except IndexError:
        return out
