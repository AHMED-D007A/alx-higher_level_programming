#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        return (0, None)
    else:
        length = len(sentence)
        first_ch = sentence[0]
        my_tuple = tuple(length, first_ch)
        return (my_tuple)
