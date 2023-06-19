#!/usr/bin/python3
"""This is the base module for this project"""


class Base:
    """this is the Base class used for other Objects(Rectangle, square)"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
