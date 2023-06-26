#!/usr/bin/python3
"""this is MyList module."""


class MyList(list):
    """this is mylist class that inherits a list and sort it."""
    def __init__(self):
        super()

    def print_sorted(self):
        h = list(self)
        h.sort()
        print(h)
