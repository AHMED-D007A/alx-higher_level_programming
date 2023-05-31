#!/usr/bin/python3
"""
this is a "Square" module.

it provides a Square class with initialization of size.
"""
class Square:
    """a simple Square module wiht initialization of size(int >= 0)"""
    def __init__(self, size = 0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
