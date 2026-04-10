#!/usr/bin/python3
"""This module defines a CountedIterator class that extends the built-in iterator."""


class CountedIterator:
    """Class that extends the built-in iterator to count the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the current count of items iterated."""
        return self.count
