#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    maxx = 0
    if len_list == 0:
        return (None)
    for i in range(len_list):
        if my_list[i] > maxx:
            maxx = my_list[i]
    return (maxx)
