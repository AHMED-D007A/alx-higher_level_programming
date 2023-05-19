#!/usr/bin/python3
def common_elements(set_1, set_2):
    out = []
    for n in set_1 & set_2:
        out += n
    return (out)
