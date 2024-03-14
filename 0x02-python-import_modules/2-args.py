#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = len(argv) - 1
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("{} argument:".format(arguments))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arguments))
        for i in range(1, arguments + 1):
            print("{}: {}".format(i, argv[i]))
