#!/usr/bin/python3
"""This module defines a function that performs a magic calculation."""
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception:
            result = a + b
            break

    return result
