#!/usr/bin/python3
""" A module that defines a script to add argument to a Python list
and save them into a (add_item.json) file."""

import sys
savefile = __import__('5-save_to_json_file').save_to_json_file
loadfile = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

exist_list = loadfile("add_item.json") if args else []
exist_list.extend(args)
savefile(exist_list, "add_item.json")
