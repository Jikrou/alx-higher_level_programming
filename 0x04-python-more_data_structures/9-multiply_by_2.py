#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return{key: int(value) * 2 for key, value in a_dictionary.items()}
