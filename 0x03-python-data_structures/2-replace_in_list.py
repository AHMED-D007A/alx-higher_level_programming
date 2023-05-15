#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (0 <= idx < len(my_list)):
        my_list.remove(my_list[idx])
        my_list.insert(idx, element)
        return (my_list)
    else:
        return (my_list)
