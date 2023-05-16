#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = list(tuple_a) + [0]*2
    sec = list(tuple_b) + [0]*2
    sum = [x + y for x, y in zip(first, sec)]
    return tuple(sum[0:2])
