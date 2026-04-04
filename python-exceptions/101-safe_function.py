#!/usr/bin/python3
"""Defines a function that safely executes a function."""
import sys
def safe_function(fct, *args):
    """Execute a function safely with error handling.

    Args:
        fct: The function to be executed.
        *args: Variable length argument list for the function.

    Returns:
        The result of the function if it executes successfully, None otherwise.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
