#!/usr/bin/python3
"""This module provides a function to execute other functions safely."""
import sys


def safe_function(fct, *args):
    """Execute a function safely and return None if an exception occurs.

    Args:
        fct: The function to execute.
        *args: Arguments to pass to the function.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
