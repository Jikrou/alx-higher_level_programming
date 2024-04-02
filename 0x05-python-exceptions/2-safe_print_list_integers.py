#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    out = 0
    for i in range(0, x):
        try:
            print("{}".format(int(my_list[i])), end="")
            out += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
    print()
    return (out)
