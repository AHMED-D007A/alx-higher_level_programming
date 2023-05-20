#!/usr/bin/python3
def common_elements(set_1, set_2):
    out = []
    for i in range(set_1):
        if (set_1[i] == set_2[i]):
            out += set_1[i]
    return (out)
