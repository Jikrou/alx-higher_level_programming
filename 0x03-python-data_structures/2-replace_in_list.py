#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if len(my_list)-1 >= idx >= 0:
            if i == idx:
                my_list[idx] = element
                return my_list
        elif idx < 0:
            return my_list
        else:
            return my_list
