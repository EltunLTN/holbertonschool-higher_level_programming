#!/usr/bin/python3
"""This module solves the N queens problem using backtracking."""
import sys


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe.

    Args:
        queens (list): List of column positions for placed queens.
        row (int): The row to place the queen.
        col (int): The column to place the queen.
    """
    for r, c in enumerate(queens):
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve(n, row, queens):
    """Solve N queens using backtracking.

    Args:
        n (int): The size of the board.
        row (int): The current row to place a queen.
        queens (list): List of column positions for placed queens.
    """
    if row == n:
        print([[r, c] for r, c in enumerate(queens)])
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve(n, row + 1, queens)
            queens.pop()


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solve(n, 0, []
