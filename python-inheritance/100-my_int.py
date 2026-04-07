#!/usr/bin/python3
"""Module that defines a MyInt class that inherits from int"""


class MyInt(int):
    """Class MyInt that inherits from int and
    has inverted equality and inequality operators"""
    def __init__(self, my_i):
        self.my_i = my_i

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
