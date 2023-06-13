#!/usr/bin/python3

"""A module that returns all the attributes of a class"""


def lookup(obj):
    """returns a list of all the attributes of the obj"""
    return dir(obj)
