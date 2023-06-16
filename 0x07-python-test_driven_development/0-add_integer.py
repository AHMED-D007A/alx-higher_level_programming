#!/usr/bin/python3
"""
this is Add integer module.

this module supplies on one function 'add_integer()'.
it add two numbers and return them to the user.
"""
def add_integer(a, b=98):
    """this module add two integers or floats and return them"""
    my_list = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    for x, y in list(zip(my_list, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))

    return int(a) + int(b)
