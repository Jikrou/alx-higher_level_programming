#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cplist = my_list[:]
    len_list = len(my_list)
    for i in range(len_list):
        if len_list >= idx >= 0:
            if i == idx:
                cplist[i] = element
                return cplist
        elif idx < 0:
            return cplist
        else:
            return cplist
