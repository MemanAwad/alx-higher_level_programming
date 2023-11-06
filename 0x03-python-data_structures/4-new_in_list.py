#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listlen = len(my_list) - 1
    listcopy = my_list.copy()
    if idx < 0 or idx > listlen:
        return (listcopy)
    else:
        listcopy[idx] = element
        return (listcopy)
