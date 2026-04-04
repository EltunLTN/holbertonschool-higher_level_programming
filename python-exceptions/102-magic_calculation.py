#!/usr/bin/python3
"""This module defines a function that performs a magic calculation."""
def magic_calculation(a, b):
    """Perform a magic calculation based on the values of a and b."""
    result = 0
    try:
        for i in range(1, 3):
            try:
                if i > a:
                    raise Exception("Too far")
                result += (a ** b) / i
            except Exception:
                result = b + a
                break
    except Exception:
        pass
    return result
