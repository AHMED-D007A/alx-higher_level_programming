#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    check_a = 2 - tuple_a
    check_b = 2 - tuple_b
    if (check_a):
        tuple_a += (0) * check_a
    if (check_b):
        tuple_b += (0) * check_b
    tuple_sum = ({x + y for x, y in zip(tuple_a, tuple_b)})
    return (tuple_sum)
