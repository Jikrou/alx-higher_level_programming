#!/usr/bin/python3
def no_c(my_string):
    cpstring = ""
    for i in my_string:
        if 'c' != i and 'C' != i:
            cpstring += i
    return cpstring
