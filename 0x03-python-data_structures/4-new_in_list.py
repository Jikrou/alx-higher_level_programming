#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cplist = my_list[:]
    len_list = len(my_list) - 1
    if len_list >= idx >= 0:
        cplist[idx] = element
        return cplist
    elif idx < 0:
        return cplist
    else:
        return cplist
