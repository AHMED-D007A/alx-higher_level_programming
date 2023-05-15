#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    elif (0 <= idx < len(my_list)):
        cp_my_list = my_list[:]
        cp_my_list.remove(cp_my_list[idx])
        cp_my_list.insert(idx, element)
        return (cp_my_list)
    else:
        return (my_list)
