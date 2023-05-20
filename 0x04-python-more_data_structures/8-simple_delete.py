#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == list(a_dictionary.keys()):
        del a_dictionary[key]
    return a_dictionary
