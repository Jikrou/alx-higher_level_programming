#!/usr/bin/python3
def print_last_digit(number):
    lastnumber = abs(number) % 10
    print(f"{lastnumber:d}", end="")
    return lastnumber
