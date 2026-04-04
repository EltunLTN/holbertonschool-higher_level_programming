#!/usr/bin/python3
"""Defines a function that safely prints an integer."""
import sys


def safe_print_integer_err(value):
    """Print an integer with error handling.

    Args:
        value: The value to be printed.

    Returns:
        True if the value is an integer and has been printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
