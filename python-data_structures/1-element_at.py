#!/usr/bin/python3
def element_at(my_list, idx):
    if idx<0:
        return None
    return f"Element at index {idx:d} is {my_list[idx]}"