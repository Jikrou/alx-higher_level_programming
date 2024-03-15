#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx >= 0:
            if i == idx:
                return my_list[i]
