#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list == None):
        return None
    else:
        max = 0
        for i in my_list:
            if (max < i):
                max = i
        return max
