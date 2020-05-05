#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return None
    if idx in my_list:
        return my_list[idx]
