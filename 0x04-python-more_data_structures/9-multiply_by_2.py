#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    new_dic = {key: int(value) * 2 for key, value in a_dictionary.items()}
    return new_dic
