#!/usr/bin/python3
"""This module defines a script that adds all arguments to a Python list"""


from sys import argv
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file_name = "add_item.json"

if not os.path.exists(file_name):
    save_to_json_file([], file_name)

new_list = load_from_json_file(file_name)

for i in range(1, len(argv)):
    new_list.append(str(argv[i]))

save_to_json_file(new_list, file_name)
