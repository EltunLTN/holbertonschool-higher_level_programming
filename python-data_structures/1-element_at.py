#!/usr/bin/python3
def element_at(my_list, idx):
    if idx<0:
        return None
    return "Element at index {:d} is {}".format(idx, my_list[idx])
