#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == None):
        return (0, None)
    else:
        length = len(sentence)
        first_ch = sentence[0]
        my_tuple = (length, first_ch)
        return (my_tuple)
