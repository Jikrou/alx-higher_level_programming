#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        if isinstance(k, dict):
            print("{}".format(k))
            for k_sub, v_sub in v.items():
                print("{}: {}".format(k_sub, v_sub))
        else:
            print("{}: {}".format(k, v))
